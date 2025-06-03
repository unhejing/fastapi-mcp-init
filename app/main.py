from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import system
from fastapi_mcp import FastApiMCP

# Create FastAPI app instance
app = FastAPI(
    title="FastAPI Project",
    description="A FastAPI project template with system monitoring capabilities",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(system.router, prefix="/api/v1")

@app.get("/")
async def root():
    """
    Root endpoint
    """
    return {"message": "Welcome to FastAPI Project"}

# Create MCP instances for different system monitoring endpoints
# 全部系统监控API
system_all_mcp = FastApiMCP(
    app,
    name="System Monitoring API",
    include_tags=["system"]
)

# Mount MCP endpoints
system_all_mcp.mount(mount_path="/system-mcp")

if __name__ == "__main__":
    import uvicorn
    print("Server is running with multiple MCP endpoints:")
    print(" - /system-mcp: All system monitoring endpoints")
    uvicorn.run(app, host="0.0.0.0", port=8000) 
    # uvicorn app.main:app --reload --host 0.0.0.0 --port 8000