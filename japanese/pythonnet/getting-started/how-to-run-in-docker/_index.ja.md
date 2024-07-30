---
title: Docker で python via .NET の Aspose.Cells を実行する方法
type: docs
description: "Linux 向けの Docker コンテナで Aspose.Cells を実行する"
weight: 140
url: /ja/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## 前書き:

多くのユーザーが当社のさまざまな製品を Docker で使用しており、さまざまな問題に遭遇しています。本記事では、Debian Linux をベースとした Docker 環境での Aspose.Cells for Python via .NET の使用方法について簡単に紹介します。

## 例:

簡単な例を使って使用法を説明します。この場合、機能は非常に簡単で、aspose_test.py に日本語テキストを含む Excel ファイルを開くだけです。ここではベースイメージとして python:3.11 を使用し、対応する Dockerfile は以下の通りです。

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

次に、次のコマンドを実行すると、最終結果が得られます。
- Dockerイメージのビルド

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Dockerイメージの実行

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- 注意:

さまざまな言語を含むExcelファイルの開くサポートのために、ICUをインストールする必要があります。Python via .NETラッパーは.NET Core 3.1に基づいており、.NET Core 3.1はICUの特定のバージョン要件を持っています。ICUのバージョンは70を超えてはならず、特定バージョンのICUをインストールする必要があります。


## 関連項目

- [Windows に Docker Desktop をインストールする](https://docs.docker.com/docker-for-windows/install/)
