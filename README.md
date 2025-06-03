# FastAPI Project

这是一个使用FastAPI框架构建的RESTful API项目。

## 功能特点

- 基于FastAPI框架
- RESTful API设计
- 包含示例API端点
- CORS支持
- 模块化的项目结构

## 项目结构

```
.
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── system.py
│   ├── core/
│   ├── schemas/
│   └── main.py
├── requirements.txt
└── README.md
```

## 安装

1. 克隆项目
2. 创建虚拟环境（推荐）
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 运行项目

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

访问 http://localhost:8000/docs 查看API文档。

## MCP配置
```
"system-mcp": {
   "url": "http://localhost:8000/system-mcp"
}
```

## 开发

1. 安装开发依赖
2. 遵循项目结构