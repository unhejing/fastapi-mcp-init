# FastAPI Project

这是一个使用FastAPI框架构建的RESTful API项目，集成了MCP (Model Context Protocol) 支持。

## 功能特点

- 基于FastAPI框架
- RESTful API设计
- MCP (Model Context Protocol) 支持
- 系统监控API示例
- CORS支持
- 模块化的项目结构

## 项目结构

```
.
├── main.py                 # FastAPI应用主入口文件
├── requirements.txt        # Python依赖包列表
├── Dockerfile              # Docker镜像构建文件
├── .dockerignore           # Docker构建忽略文件
├── README.md              # 项目说明文档
└── sample/                # MCP接口模块目录
    ├── api.py             # 系统监控API路由定义
    ├── schemas.py         # 数据模型定义
    └── utils.py           # 工具函数
```

## 安装

1. 克隆项目
2. 创建虚拟环境（推荐）：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   venv\Scripts\activate     # Windows
   ```
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 运行项目

### 本地开发运行

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8023
```

访问 http://localhost:8023/docs 查看API文档。

### Docker 部署

#### 构建镜像

```bash
docker build -t fastapi-mcp-app:latest .
```

或者同时构建多个标签：

```bash
docker build -t fastapi-mcp-app:latest -t fastapi-mcp-app:1.0.0 .
```

#### 运行容器

```bash
docker run -d -p 8023:8023 --name fastapi-mcp fastapi-mcp-app:latest
```

#### 使用 Docker Compose（可选）

创建 `docker-compose.yml` 文件：

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8023:8023"
    container_name: fastapi-mcp
    restart: unless-stopped
```

然后运行：

```bash
docker-compose up -d
```

#### 查看日志

```bash
docker logs -f fastapi-mcp
```

#### 停止容器

```bash
docker stop fastapi-mcp
docker rm fastapi-mcp
```

访问 http://localhost:8023/docs 查看API文档。

## MCP配置

当前已配置的MCP接口：

```json
{
  "system-mcp": {
    "url": "http://localhost:8023/system-mcp"
  }
}
```

### 添加新的MCP接口

如需添加新的MCP接口，请在 `sample/` 目录下创建新的子目录，例如：

```
sample/
├── system/          # 系统监控接口（当前）
│   ├── __init__.py
│   ├── api.py
│   ├── schemas.py
│   └── utils.py
└── your-new-mcp/    # 新的MCP接口目录
    ├── __init__.py
    ├── api.py
    ├── schemas.py
    └── utils.py
```

然后在 `main.py` 中：
1. 导入新的路由
2. 注册路由到FastAPI应用
3. 创建并挂载新的MCP实例

示例：
```python
from sample.your_new_mcp.api import router as your_router

app.include_router(your_router, prefix="/api/v1")

your_mcp = FastApiMCP(
    app,
    name="Your New MCP API",
    include_tags=["your-tag"]
)
your_mcp.mount_http(mount_path="/your-new-mcp")
```

## API端点

### 系统监控API

- `GET /api/v1/system/info` - 获取系统信息（CPU、内存、磁盘）
- `GET /api/v1/system/load` - 获取系统负载（CPU、内存、磁盘I/O、网络I/O）

## 开发

1. 遵循项目结构，新的MCP接口在 `sample/` 目录下创建子目录
2. 使用Pydantic定义数据模型
3. 使用FastAPI的标签系统组织API端点
4. 确保每个MCP接口都有对应的路由和MCP挂载点