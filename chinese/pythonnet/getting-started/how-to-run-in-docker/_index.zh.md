---
title: 如何在Docker中运行Aspose.Cells for Python via .NET
type: docs
description: "在Linux的Docker容器中运行Aspose.Cells"
weight: 140
url: /zh/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## 前言：

越来越多的用户在Docker中使用我司的各类产品，他们遇到各种问题。本文将简要介绍如何在基于Debian Linux的Docker环境中使用Aspose.Cells for Python via .NET。

## 示例：

我们用一个简单的例子来说明用法。在这种情况下，功能非常简单，只是在aspose_test.py中打开包含日文文本的Excel文件。这里，我们以python:3.11作为基础镜像，相应的Dockerfile如下：

{{< highlight plain >}}
FROM python:3.11 AS base

# For drawing,e.g. convert to PDF
RUN apt-get update && apt-get install -y libgdiplus

# Install ICU version supported by .NET Core 3.1
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu70_70.1-2_amd64.deb
RUN dpkg -i libicu70_70.1-2_amd64.deb

RUN pip install -i aspose-cells-python
CMD ["python", "aspose_test.py"]
{{< /highlight >}}

然后，当我们运行以下命令时，会得到最终结果：
- 构建Docker镜像

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- 运行Docker镜像

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- 注意：

为了支持打开包含多种语言的Excel文件，我们需要安装ICU。考虑到Python via .NET封装基于.NET Core 3.1，而.NET Core 3.1对ICU有特定版本要求，不应超过版本70，我们需要安装特定版本的ICU。


## 另请参阅

- [在Windows上安装Docker Desktop](https://docs.docker.com/docker-for-windows/install/)
