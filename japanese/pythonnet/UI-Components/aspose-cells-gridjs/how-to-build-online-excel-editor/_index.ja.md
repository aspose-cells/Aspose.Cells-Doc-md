---
title: DockerでAspose.Cells.GridJsを実行する方法
type: docs
weight: 250
url: /ja/python-net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs、docker
description: この記事は、オンラインExcelエディタまたはビューアアプリケーションを構築するために、Docker内でGridJsを実行する方法を紹介します。
aliases:
  - /python-net/aspose-cells-gridjs/docker/
  - /python-net/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /python-net/aspose-cells-gridjs/run-gridjs-in-docker/
  - /python-net/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# Dockerガイド

## 前提条件

お使いのマシンにDockerをインストールしていることを確認してください。Dockerは[公式Dockerウェブサイト](https://www.docker.com/get-started)からダウンロードしてインストールできます。

## ステップ1：Dockerfileを作成

あなたのプロジェクト [ディレクトリ](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs) に `Dockerfile` という名前のファイルを作成してください。`Dockerfile` にはDockerイメージのビルド方法を記述します。

## ステップ2: GridJs用のDockerfileを書く

こちらはPythonアプリケーションを備えたGridJsデモ用の [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs/Dockerfile) の例です。

```dockerfile
# use Python 3.13 as parent image
FROM python:3.13-slim
# web port
EXPOSE 2022

# Update the package list and install the   package along with additional related packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libicu-dev \
        icu-devtools \
        pkg-config \
        build-essential \
	fontconfig \ 
        libgdiplus && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# Set the necessary environment variable  
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu
# Set the System.Globalization.Invariant setting to true
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true

WORKDIR /app  

# copy all to  /app  
COPY . /app  


RUN pip install --no-cache-dir -r requirements.txt  
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the file path to store the uploaded files
RUN mkdir -p /app/uploads
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache/  
COPY wb/*.xlsx /app/wb/



# start cmd
CMD [ "python", "./main.py" ]
```

## ステップ 3: Dockerイメージのビルド
Dockerイメージのビルド：ターミナルから次のコマンドを実行してDockerイメージを作成します：
```bash
docker build -t gridjs-demo-python .
```
`gridjs-demo-python`を、自分のDockerイメージの名前に置き換えることができます。

## ステップ 4: Dockerコンテナの実行
イメージが作成されたら、次のコマンドを使用してコンテナを実行できます：

```bash
docker run -d -p 2022:2022   -v C:/path/to/license.txt:/app/license  --name gridjs-demo-container  gridjs-demo-python
```

または、デモをトライアルモードで実行するだけです：


```bash
docker run -d -p 2022:2022 --name gridjs-demo-container  gridjs-demo-python
```

Docker実行コマンドオプションの説明
-d: コンテナをデタッチモード（バックグラウンド）で実行します。
-p 2022:2022：コンテナのポート2022をホストマシンのポート2022にマッピングします。
-v C:/path/to/license.txt:/app/license: ホストマシンのライセンスファイルのパスをコンテナ内のファイルパスにマッピングします。
--name gridjs-demo-container: コンテナに名前を割り当てます。

## ステップ 5: コンテナが実行中か確認する
コンテナが稼働しているかどうかを確認するには、次のコマンドを使用してください：

```bash
docker ps
```
これにより、すべての実行中のコンテナがリストされます。あなたのコンテナが名前とステータスとともに表示されるはずです。

## ステップ 6: Webアプリケーションへアクセスする

Webブラウザを開き、`http://localhost:2022`にアクセスしてください。アプリケーションが動作しているはずです。

## 追加コマンド

### コンテナの停止

実行中のコンテナを停止するには、次のコマンドを使用します：

```bash
docker stop gridjs-demo-container
```

### コンテナの削除
停止したコンテナを削除するには、次のコマンドを使用します：

```bash
docker rm  gridjs-demo-container
```

### イメージの削除
イメージを削除するには、次のコマンドを使用します：

```bash
docker rmi gridjs-demo-python
```




