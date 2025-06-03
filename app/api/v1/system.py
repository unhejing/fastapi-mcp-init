from fastapi import APIRouter
import psutil
from app.schemas.system_schema import SystemInfo, SystemLoad

router = APIRouter(
    prefix="/system",
    tags=["system"]
)

@router.get(
    "/info",
    response_model=SystemInfo,
    operation_id="get_system_info",
    summary="Get System Information",
    description="""
    Retrieve detailed system information including:
    - CPU configuration and usage
    - Memory (RAM) statistics
    - Disk space information
    
    This endpoint provides a snapshot of the current system resources.
    """
)
async def get_system_info():
    """
    Get comprehensive system information including CPU, memory and disk details.
    
    Returns:
        SystemInfo: Detailed system metrics including CPU, memory, and disk information
    """
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return SystemInfo(
        cpu_count=psutil.cpu_count(),
        cpu_percent=psutil.cpu_percent(),
        memory_total=memory.total,
        memory_available=memory.available,
        memory_percent=memory.percent,
        disk_total=disk.total,
        disk_used=disk.used,
        disk_free=disk.free,
        disk_percent=disk.percent
    )

@router.get(
    "/load",
    response_model=SystemLoad,
    operation_id="get_system_load",
    summary="Get System Load",
    description="""
    Retrieve real-time system load metrics including:
    - Current CPU usage
    - Current memory usage
    - Disk I/O statistics
    - Network I/O statistics
    
    This endpoint provides real-time performance metrics for monitoring system load.
    """
)
async def get_system_load():
    """
    Get current system load including CPU, memory, disk I/O and network usage.
    
    Returns:
        SystemLoad: Real-time system load metrics including CPU, memory, disk and network usage
    """
    disk_io = psutil.disk_io_counters()
    network = psutil.net_io_counters()
    
    return SystemLoad(
        cpu_percent=psutil.cpu_percent(),
        memory_percent=psutil.virtual_memory().percent,
        disk_io_read=disk_io.read_bytes,
        disk_io_write=disk_io.write_bytes,
        network_bytes_sent=network.bytes_sent,
        network_bytes_recv=network.bytes_recv
    ) 