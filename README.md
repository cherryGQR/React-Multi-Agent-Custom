# React-Multi-Agent-Custom
### 英文版 README.md

```markdown
# EFA Multi-Agent Failure Analysis System

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A sophisticated multi-agent system for chip failure analysis in semiconductor testing environments, built on the ReAct (Reasoning + Acting) framework.

## 🚀 Features

- **Multi-Agent Architecture**: Recursive hierarchical agent framework for complex task decomposition
- **ReAct Pattern**: Reasoning + Acting loop for transparent decision-making
- **Human-in-the-Loop**: Seamless integration of human feedback in critical decision points
- **Semantic Search**: Advanced database querying for failure pattern recognition
- **Real-time Monitoring**: Observable agent states and execution tracing

## 🏗 System Architecture

```
MultiAgentSystem/
├── agents/                 # Core agent implementations
│   ├── plan_agent.py      # Task decomposition & workflow coordination
│   ├── action_agent.py    # Tool dispatching & sub-agent execution
│   ├── observation_agent.py # Execution monitoring & human interaction
│   ├── reflection_agent.py # Performance evaluation & strategy adjustment
│   └── human_feedback.py  # Human-in-the-loop integration
├── config/                # LLM configurations & prompt templates
├── models/               # Data models & state management
├── tools/               # Sub-agents & utility functions
└── main.py             # System orchestration
```

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/cherryGQR/React-MultiAgent.git
   cd React-MultiAgent.git
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # OR
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

## 🎯 Quick Start

```python
import asyncio
from main import MultiAgentSystem

async def main():
    # Initialize the multi-agent system
    system = MultiAgentSystem()
    
    # Create analysis task
    task_description = ""
    task_id = system.create_task(task_description)
    
    # Execute analysis
    result = await system.execute_task(task_id)
    print(f"Final result: {result.result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## 🔧 Configuration

### LLM Settings
Configure your language model in `config/models.py`:

```python
LLM_CONFIGS = {
    "model": {
        "model": "model",
        "api_key": "your_api_key",
        "base_url": "",
        "temperature": 0.7
    }
}
```

## 🤖 Agent Workflow

1. **Planning Phase**: Task decomposition and agent assignment
2. **Execution Phase**: Sub-agent invocation and tool execution  
3. **Observation Phase**: Result monitoring and human interaction
4. **Reflection Phase**: Performance evaluation and strategy adjustment

## 🌐 API Integration

### Custom Tool Integration
```python
from tools.base_sub_agent import SubAgentBase

class CustomAnalysisAgent(SubAgentBase):
    async def process(self, query: str, context: List[Message] = None) -> str:
        # Implement custom analysis logic
        return analysis_result
```

## 🧪 Testing

Run the test suite:
```bash
pytest tests/ -v
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on the ReAct agent framework principles
- Inspired by modern multi-agent systems research
- Thanks to the semiconductor testing community for domain expertise
```

### 中文版 README_zh.md

```markdown
# 多智能体系统

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

第一个基于ReAct框架构建的自定义分析多智能体系统，可在此基础上灵活设计，不再基于固定框架，强落地实战。

## 🚀 核心特性

- **多智能体架构**: 递归层级智能体框架，支持复杂任务分解
- **ReAct模式**: 推理+执行的透明决策循环
- **人机协同**: 关键决策点的人类反馈无缝集成
- **语义搜索**: 先进的失效模式识别数据库查询
- **实时监控**: 可观测的智能体状态与执行追踪

## 🏗 系统架构

```
MultiAgentSystem/
├── agents/                 # 核心智能体实现
│   ├── plan_agent.py      # 任务分解与工作流协调
│   ├── action_agent.py    # 工具调度与子代理执行
│   ├── observation_agent.py # 执行监控与人机交互
│   ├── reflection_agent.py # 效果评估与策略调整
│   └── human_feedback.py  # 人类反馈集成
├── config/                # LLM配置与提示词模板
├── models/               # 数据模型与状态管理
├── tools/               # 子代理与工具函数
└── main.py             # 系统编排
```

## 📦 安装指南

1. **克隆仓库**
   ```bash
   git clone https://github.com/cherryGQR/React-MultiAgent.git
   cd React-MultiAgent.git
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   venv\Scripts\activate    # Windows
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **环境配置**
   ```bash
   cp .env.example .env
   # 编辑.env文件配置API密钥和端点
   ```

## 🎯 快速开始

```python
import asyncio
from main import MultiAgentSystem

async def main():
    # 初始化多智能体系统
    system = MultiAgentSystem()
    
    # 创建分析任务
    task_description = ""
    task_id = system.create_task(task_description)
    
    # 执行分析
    result = await system.execute_task(task_id)
    print(f"最终结果: {result.result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## 🔧 配置说明

### LLM 设置
在 `config/models.py` 中配置语言模型：

```python
LLM_CONFIGS = {
    "model": {
        "model": "model",
        "api_key": "您的API密钥",
        "base_url": "",
        "temperature": 0.7
    }
}
```

## 🤖 智能体工作流

1. **规划阶段**: 任务分解与智能体分配
2. **执行阶段**: 子代理调用与工具执行
3. **观察阶段**: 结果监控与人机交互  
4. **反思阶段**: 性能评估与策略调整

## 🌐 API 集成

### 自定义工具集成
```python
from tools.base_sub_agent import SubAgentBase

class CustomAnalysisAgent(SubAgentBase):
    async def process(self, query: str, context: List[Message] = None) -> str:
        # 实现自定义分析逻辑
        return analysis_result
```

## 🧪 测试

运行测试套件：
```bash
pytest tests/ -v
```

## 🤝 贡献指南

我们欢迎各种贡献！请查看[贡献指南](CONTRIBUTING.md)了解详情。

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m '添加特性'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 基于ReAct智能体框架原则构建
- 受现代多智能体系统研究启发
```

## 🔄 关键改进建议

基于开源项目最佳实践，我建议：

### 1. 项目结构优化
```python
MultiAgent/
├── docs/                    # 项目文档
├── tests/                   # 测试用例
├── examples/               # 使用示例
├── docker/                 # 容器化配置
└── scripts/               # 部署脚本
```

### 2. 配置管理改进
```python
# config/settings.py
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings with environment variable support"""
    app_name: str = "Multi-Agent System"
    max_iterations: int = 100
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
```

### 3. 错误处理增强
```python
# utils/exceptions.py
class MultiAgentError(Exception):
    """Base exception for multi-agent system"""
    pass

class LLMConnectionError(MultiAgentError):
    """LLM service connection issues"""
    pass

class InvalidAgentStateError(MultiAgentError):
    """Invalid agent state transition"""
    pass
```

