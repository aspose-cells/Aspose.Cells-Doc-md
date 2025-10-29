---
title: 使用 C++ 通过 Golang 的 Aspose.Cells for Go 与 Excelize、Tealeg/xlsx 和 Go OLE 在功能和性能上的对比
linktitle: 功能和性能的对比
type: docs
weight: 40
url: /zh/go-cpp/comparison-of-functionality-and-performance/
description: 使用 C++ 通过 Golang 的 Aspose.Cells for Go 与 Excelize、Tealeg/xlsx 和 Go OLE 在功能和性能上的对比
keywords: Aspose.Cells、Excel、公式监视窗口、单元格、添加、C++
---

以下是 Aspose.Cells for Go（通过 C）与其他主流 Golang Excel 处理库（Excelize、tealeg/xlsx、go-ole）在功能、性能和使用场景方面的综合对比

## 基本定位和结构的差异

| 库名称             | 类型                        | 底层实现                       | CGO依赖                | 跨平台部署 |
| :------------------- | :----------------------------- | :--------------------------------- | :----------------------- | :-----------------------  |
| Aspose.Cells for Go  | 商业库（MIT/付费）          | 原生引擎，Go CGO封装             |  ✅  是             | 支持 Windows、Linux |
| Excelize          | 开源库（MIT）                | 纯Go实现                        |  ❌  否             | 支持 Windows、Linux、MacOS |
| tealeg/xlsx       | 开源库（BSD）                | 纯Go实现                        |  ❌  否             | 支持 Windows、Linux、MacOS |
| go-ole            | 开源库（BSD）                | Go Windows OLE/COM 接口           |  ✅  是（仅Windows） | 仅Windows |

### 关键差异

- Aspose.Cells for Go via C++ 是一款工业级商用库，功能最完善，但需要付费。
- Excelize 目前是最活跃且开源的Go库，纯Go实现。
- Tealeg/xlsx 是较早的开源库，功能较基础，维护较慢。
- Go-ole 是一种仅适用于Windows的COM自动化方案，依赖Excel安装，不建议用于服务器环境。

## 功能比较

### 支持的文件格式比较

| 电子表格格式             |   Aspose.Cells for Go via C++ | Excelize     | Tealeg/xlsx | Go-OLE（Excel应用） |
| :--------------------- | :---------------------------- | :---------- | :---------- | :-------------------  |
| Xlsx                   | ✅ 是                         | ✅ 是      | ✅ 是       | 依赖Excel |
| Xlsb                   | ✅ 是                         | ❌ 否      | ❌ 否       | 依赖Excel |
| Xls                    | ✅ 是                         | ❌ 否      | ❌ 否       | 依赖Excel |
| Xlsm                   | ✅ 是                         | ✅ 是      | ✅ 是       | 依赖Excel |
| Xltm                   | ✅ 是                         | ✅ 是      | ✅ 是       | 依赖Excel |
| Xltx                   | ✅ 是                         | ✅ 是      | ✅ 是       | 依赖Excel |
| Csv                    | ✅ 是                         | ❌ 否      | ❌ 否       | 依赖Excel |
| Ods                    | ✅ 是                         | ❌ 否      | ❌ 否       | 依赖Excel |
| Html                   | ✅ 是                         | ❌ 否      | ❌ 否       | ❌ 否      |
| Numbers                | ✅ 是                         | ❌ 否      | ❌ 否       | ❌ 否      |
| Json                   | ✅ 是                         | ❌ 否      | ❌ 否       | ❌ 否      |
| Xml                    | ✅ 是                         | ❌ 否      | ❌ 否       | ❌ 否      |
| 电子表格ML             | ✅ 是                         | ❌ 否      | ❌ 否       | ❌ 否      |

### 支持的电子表格功能

| 库功能                     |   Aspose.Cells for Go via C++ | Excelize        | Tealeg/xlsx | Go-OLE（Excel应用） |
| :----------------------------    | :---------------------------- | :--------------- | :---------- | :----------  |
| 读写（支持文件格式）        | ✅ 是                         | ✅ 是       | ✅ 是      | ✅ 是  |
| 单元格/行/列/工作表        | ✅ 是                         | ✅ 是       | ✅ 是      | ✅ 是  |
| 样式 | ✅ 是 | ✅ 是 | ✅ 是 | ✅ 是 |
| 公式计算 | ✅ 是 | ✅ 部分 | ❌ 否 | ✅ 由Excel计算 |
| 图表/图片 | ✅ 是 | ✅ 部分 | ❌ 否 | ✅ 是 |
| 透视表 | ✅ 是 | ✅ 是 | ❌ 否 | ✅ 是 |
| 条件格式 | ✅ 是 | ✅ 是 | ❌ 否 | ✅ 是 |
| 数据验证 | ✅ 是 | ✅ 是 | ❌ 否 | ✅ 是 |
| 加密/密码保护 | ✅ 是 | ✅ 是 | ❌ 否 | ✅ 是 |
| 数据验证 | ✅ 是 | ✅ 是 | ❌ 否 | ✅ 是 |
| VBA宏 | ✅ 是（已阅读） | ❌ 否 | ❌ 否 | ✅ 是 |
| 数据验证 | ✅ 是 | ✅ 是 | ❌ 否 | ✅ 是 |

## 性能比较

- **测试环境**：
处理器：第12代英特尔® 酷睿™ i7-12700（2.10 GHz）
已装RAM：64.0 GB（可用63.7 GB）
操作系统：Microsoft Windows 11 专业版
操作系统版本：10.0.26100
操作系统架构：64位
Go版本：go version go1.24.5 windows/amd64
Aspose.Cells for Go via C++：25.9.0
Excelize：1.4.1

- **测试场景**：假设一个大文件，10个工作表，100,000行 x 250列，包括格式

- **运行结果**：
  - Excelize运行了35分钟（开始时间：2025-10-09T10:04:16+08:00，结束时间：2025-10-09T10:39:53+08:00），生成文件大小：1.11 GB。
  - Aspose.Cells for Go via C++（模型1）运行了27分钟（开始时间：2025-10-09T10:57:55+08:00，结束时间：2025-10-09T11:16:24+08:00），生成文件大小：936MB。
  - Aspose.Cells for Go via C++（模型2）运行了16分钟（开始时间：2025-10-09T12:01:26+08:00，结束时间：2025-10-09T12:17:17+08:00），生成文件大小：1.16GB。
