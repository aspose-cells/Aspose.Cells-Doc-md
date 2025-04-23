---
title: 版本控制
type: docs
weight: 40
url: /zh/go-cpp/versioning/
description: 如何安装 Aspose Cells for Go via C++ 并创建“Hello World”应用程序。
---

**github.com/aspose-cells/aspose-cells-go-cpp/v25** 是一个指向第三方库特定版本的 Go 模块路径。以下对该模块路径进行拆解说明其含义：
拆解模块路径

1. **GitHub 仓库地址**：github.com/aspose-cells/aspose-cells-go-cpp

- 这部分表明该库托管在 GitHub 上，属于 aspose-cells 组织或用户，存放在名为 aspose-cells-go-cpp 的仓库中。
- Aspose.Cells 是一套用于处理和操作电子表格文件（如 Excel）的API。

1. **版本号**：/v25

- /v25 表示这是该库的第 24 版。在 Go 模块中支持语义化版本控制（SemVer），路径中包含 /vN 用于明确指定主版本号。
- 当主版本大于等于 2 时，模块路径必须包含版本号以确保兼容性和不同主版本之间的隔离。

### **含义**

- **aspose-cells-go-cpp**：这是一个 C++ 库的 Go 语言绑定，可以在 Go 程序中使用 Aspose.Cells 的功能，读取、写入和操作 Excel 文件等。
- **v25**：表示你引用的是第 24 版的库。不同的主版本可能引入不兼容的变化，因此指定版本号对于确保你的项目依赖正确的 API 和行为至关重要。

### **用法**

在你的 Go 项目中使用 aspose-cells-go-cpp v25 时，需在你的项目的 go.mod 文件中添加以下内容：

```Go
require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.x.x
```

用 go get 命令可以自动添加和下载此依赖，替换 v25.x.x 为具体的小版本和补丁版本，例如 v25.0.0：

```Go
go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.x.x
```
