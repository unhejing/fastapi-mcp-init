from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sample.api import router as system_router
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
app.include_router(system_router, prefix="/api/v1")

@app.get("/")
async def root():
    """
    Root endpoint
    """
    return {"message": "Welcome to FastAPI Project"}



# Create MCP instances for different monitoring endpoints
# 系统监控API
system_mcp = FastApiMCP(
    app,
    name="System Monitoring API",
    include_tags=["system"]
)

# Mount MCP endpoints
system_mcp.mount_http(mount_path="/system-mcp")

if __name__ == "__main__":
    import uvicorn
    print("Server is running with multiple MCP endpoints:")
    print(" - /system-mcp: System monitoring endpoints")
    uvicorn.run(app, host="0.0.0.0", port=8000) 
    # uvicorn main:app --reload --host 0.0.0.0 --port 8000