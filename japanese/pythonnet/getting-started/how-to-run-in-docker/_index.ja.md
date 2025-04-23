---
title: DockerでAspose.Cells for Python via .NETを実行する方法
type: docs
description: 「Linux用DockerコンテナでAspose.Cellsを実行する」
weight: 140
url: /ja/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## はじめに：

ますます多くのユーザーが当社のさまざまな製品をDockerで使用しており、さまざまな問題に直面しています。この記事では、Debian Linux上のDocker環境でAspose.Cells for Python via .NETを使用する方法を簡単に紹介します。

## 例：

簡単な例を用いて使用方法を説明します。この場合、機能は非常にシンプルで、aspose_test.py内の日本語を含むExcelファイルを開くだけです。ここでは、ベースイメージとしてpython:3.11を使用し、対応するDockerfileは以下の通りです。

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

次に、以下のコマンドを実行すると最終結果が得られます：
- Dockerイメージのビルド

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Dockerイメージの実行

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- 注：

さまざまな言語を含むExcelファイルを開くサポートには、ICUのインストールが必要です。Python via .NETラッパーは.NET Core 3.1に基づいており、.NET Core 3.1はICUの特定のバージョン要件を持っているため、バージョン70を超えない必要があります。そのため、特定のバージョンのICUをインストールする必要があります。


## 関連項目

- [Windows に Docker Desktop をインストールする](https://docs.docker.com/docker-for-windows/install/)
