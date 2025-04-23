---
title: Gunicorn+Flask環境でAspose.Cells for Python via Javaを使用する方法
type: docs
weight: 40
url: /ja/python-java/aspose-cells-python-java-in-gunicorn-flask/
description: このセクションでは、PythonのAspose.Cells via Javaコンポーネントと他のExcel Python操作ライブラリを比較します。
keywords: Python Excel、Excel Python、Excel Python via Java、Python via Java Excel、Python via JavaのAspose.Cellsについて、なぜ、なぜxlrd xlwt xlutils xlwings openpyxl xlswriter win32com DataNitro pandasではないか。
---

{{% alert color="primary" %}}

この初心者向けトピックでは、Aspose.Cells for Python via Javaを使用して簡単なアプリケーション（Hello World）を作成する方法を説明します。このアプリケーションは、ワークシートの指定されたセルにHello Worldという文字列を含むMicrosoft Excelファイルを作成します。

{{% /alert %}}



## **完全な環境準備**

このガイドの実行環境はUbuntu 20.04です。ご自身の状況に応じて調整してください。例が正常に動作するように、必要なツールを環境にインストールする必要があります。以下は、その手順概要です。これはあくまで大まかなガイドであり、システムや必要に応じて詳細は異なる場合があります。

### Python

インストールされていない場合は、次のようにインストールしてください：
```
sudo apt install python3 python3-pip # Ubuntu/Debian
#sudo yum install python3 python3-pip # CentOS/RHEL
```
バージョンを確認
```
python3 --version
pip3 --version
```

### Java
インストールされていない場合は、次のようにインストールしてください：
```
sudo apt install openjdk-11-jdk # Ubuntu/Debian
#sudo yum install java-17-openjdk # CentOS/RHEL
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
```
バージョンを確認
```
java -version
```

### virtualenv 仮想環境
仮想環境は実際のニーズに基づいてインストールされます。開発と運用の両方でプロジェクトの依存関係を管理するために仮想環境の使用を推奨します。
以下のコマンドに従ってインストールしてください：
```
sudo apt install python3-venv # Ubuntu/Debian
#sudo yum install python3-venv # CentOS/RHEL
```
仮想環境を作成する
```
python3 -m venv myenv # Create a virtual environment named myenv in the current directory
```
仮想環境を起動する
```
source myenv/bin/activate
```

***注意：仮想環境を使用している場合、次の操作を行う前に対応する仮想環境をアクティブにしてください***

### Flask
インストールされていない場合、次のコマンドに従ってインストールしてください：
```
pip install Flask
```

### Gunicorn
インストールされていない場合、次のコマンドに従ってインストールしてください：
```
pip install gunicorn
```

### Jpype
インストールされていない場合、次のコマンドに従ってインストールしてください：
```
pip install jpype1
```

### aspose-cells
インストールされていない場合、次のコマンドに従ってインストールしてください：
```
pip install aspose-cells
```

## **Hello Worldアプリケーションの作成**

Aspose.Cells APIを使用してHello Worldアプリケーションを作成するには：

1. [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)クラスのインスタンスを作成します。
1. ライセンスを適用：
   1. ライセンスを購入している場合は、ライセンスを使用してアプリケーションにAspose.Cellsの完全機能にアクセスします。
   1. コンポーネントの評価版を使用している場合（ライセンスなしでAspose.Cellsを使用している場合）は、このステップをスキップします。
1. 新しいMicrosoft Excelファイルを作成するか、追加/更新したい既存のファイルを開きます。
1. Microsoft Excelファイルのワークシートの任意のセルにアクセスします。
1. アクセスしたセルに**Hello World!**の単語を挿入します。
1. 変更されたMicrosoft Excelファイルを生成します。

以下の例は上記の手順を示しています。

### **ワークブックの作成**

以下の例では、新しいワークブックをゼロから作成し、最初のワークシートのセルA1に"Hello World!"という単語を書き込み、ファイルを保存します。

テストパス"/app"を持っていると仮定します。このテストパスの下で次の作業を完了します。

#### Flaskアプリケーションファイル：hello.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask1.py" >}}


#### カスタムGunicorn起動クラスファイル：custom_gunicorn.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask2.py" >}}

#### サービスの起動

サービスに必要なすべてのパッケージがインストールされていることを確認し、その後サービスを起動します。

python3-venv仮想環境を使用する場合は、テストパスに仮想環境を作成し、それを起動し、必要なツールパッケージをすべてインストールする必要があります。

``` 
python custom_gunicorn.py Or python3 custom_gunicorn.py
``` 

#### 結果の確認

1 ブラウザを開いて http://127.0.0.1:5000/ にアクセスします。

2 保存したいファイル名を入力ボックスに入力します。

3 「Generate」ボタンをクリックしてファイルを保存します。

これを行った後、入力した内容に基づくExcelファイルが現在のテストパスに保存されます。プレビュー効果は以下の通りです：

![todo:image_alt_text](HelloWorldFileInFlask.png)


## Dockerの使用例

または、上記の操作をDockerコンテナに組み込むこともできます。Dockerを使用して例の環境を構築するのは非常に簡単です。必要な操作をDockerfileに記述してください。

参考用のDockerfileの例です。環境を構築するために必要なツールキットをいくつかリストアップしています。

### Dockerfile

``` 
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    openjdk-11-jdk \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "custom_gunicorn.py"]
```

### requirements.txt

このファイルは主にPythonプロジェクトの依存関係環境を提供するために使用されます。このファイルのバージョンを必要に応じて変更できます。

```
aspose-cells==24.11.0
jpype1==1.5.1
Flask==3.0.3
gunicorn==23.0.0
```
### 主要なファイル

主なファイル構造は以下の通りです：
```
app/
|-requirements.txt
|-hello.py
|-custom_gunicorn.py
```

### コンテナの起動

次のコマンドを使用してコンテナを起動できます
```
docker run --rm -p 127.0.0.1:5000:5000 gunicorn_flask:v1.0 # gunicorn_flask:v1.0 - Image built by Dockerfile
```
