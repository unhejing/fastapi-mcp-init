from pydantic import BaseModel, Field

class SystemInfo(BaseModel):
    cpu_count: int = Field(
        description="Number of CPU cores (logical processors)"
    )
    cpu_percent: float = Field(
        description="Current CPU utilization percentage (0-100%)",
        ge=0,
        le=100
    )
    memory_total: int = Field(
        description="Total physical memory (RAM) in bytes"
    )
    memory_available: int = Field(
        description="Available memory in bytes"
    )
    memory_percent: float = Field(
        description="Memory usage percentage (0-100%)",
        ge=0,
        le=100
    )
    disk_total: int = Field(
        description="Total disk space in bytes"
    )
    disk_used: int = Field(
        description="Used disk space in bytes"
    )
    disk_free: int = Field(
        description="Free disk space in bytes"
    )
    disk_percent: float = Field(
        description="Disk usage percentage (0-100%)",
        ge=0,
        le=100
    )

    class Config:
        json_schema_extra = {
            "example": {
                "cpu_count": 8,
                "cpu_percent": 45.2,
                "memory_total": 17179869184,
                "memory_available": 8589934592,
                "memory_percent": 50.0,
                "disk_total": 512110190592,
                "disk_used": 256055095296,
                "disk_free": 256055095296,
                "disk_percent": 50.0
            }
        }

class SystemLoad(BaseModel):
    cpu_percent: float = Field(
        description="Real-time CPU utilization percentage (0-100%)",
        ge=0,
        le=100
    )
    memory_percent: float = Field(
        description="Real-time memory usage percentage (0-100%)",
        ge=0,
        le=100
    )
    disk_io_read: int = Field(
        description="Number of bytes read from disk since boot"
    )
    disk_io_write: int = Field(
        description="Number of bytes written to disk since boot"
    )
    network_bytes_sent: int = Field(
        description="Number of bytes sent through network interfaces since boot"
    )
    network_bytes_recv: int = Field(
        description="Number of bytes received through network interfaces since boot"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "cpu_percent": 35.5,
                "memory_percent": 65.2,
                "disk_io_read": 1024000,
                "disk_io_write": 2048000,
                "network_bytes_sent": 500000,
                "network_bytes_recv": 1000000
            }
        } 