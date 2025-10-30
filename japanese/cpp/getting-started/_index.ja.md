---
title: はじめに
type: docs
weight: 10
url: /ja/cpp/getting-started/
description: Aspose Cells for C++ をインストールして Hello World アプリケーションを作成する方法
---

{{% alert color="primary" %}} 

このページでは、Aspose Cells for C++ をインストールして Hello World アプリケーションを作成する方法を説明します。

{{% /alert %}}

## **インストール**

### **NuGet を通じて Aspose Cells をインストールする**

NuGet は、最も簡単な方法で Aspose.Cells for C++ をダウンロードしてインストールする方法です。 
1. C++ の Microsoft Visual Studio プロジェクトを作成します。
2. "Aspose.Cells.h" ヘッダーファイルをインクルードします。
3. Microsoft Visual Studio および NuGet パッケージマネージャーを開きます。
4. "aspose.cells.cpp" を検索して、必要な Aspose.Cells for C++ を見つけます。 
5. "インストール" をクリックすると、Aspose.Cells for C++ がダウンロードされ、プロジェクトに参照されます。

**![NuGet を介した Aspose Cells のインストール](InstallThroughNuget.png)**

また、nuget web ページから aspose.cells をダウンロードすることもできます: 
[Aspose.Cells for C++ NuGet パッケージ](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[詳細な手順](/cells/ja/cpp/installation/)については、こちら

### **Windows 上で Aspose.Cells for C++ を使用するデモ**

1. 次のページから Aspose.Cells for C++ をダウンロードします:
[Windows 用 Aspose.Cells for C++ をダウンロード](https://downloads.aspose.com/cells/cpp/)
2. パッケージを解凍すると、Aspose.Cells for C++ の使用方法に関する例が含まれています。
3. example.sln を Visual Studio 2017 またはそれ以上のバージョンで開きます
4. main.cpp: このファイルには Aspose.Cells for C++ をテストするためのコーディングが示されています

### **Linux 上で Aspose.Cells for C++ を使用するデモ**

1. 次のページから Aspose.Cells for C++ をダウンロードします:
[Linux 用 Aspose.Cells for C++ をダウンロード](https://downloads.aspose.com/cells/cpp/)
2. パッケージを解凍すると、Linux での Aspose.Cells for C++ の使用方法に関する例が含まれています。
3. 例がある場所に移動していることを確認します。
4. "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release" を実行します
5. "cmake --build example/build" を実行します

### **Mac OS 上で Aspose.Cells for C++ を使用するデモ**

1. 次のページから Aspose.Cells for C++ をダウンロードします:
[MacOS 用 Aspose.Cells for C++ をダウンロード](https://downloads.aspose.com/cells/cpp/)
2. パッケージを解凍すると、MacOS での Aspose.Cells for C++ の使用方法に関する例が含まれています。
3. 例がある場所に移動していることを確認します。
4. "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release" を実行します
5. "cmake --build example/build" を実行します

## **Hello Worldアプリケーションの作成**

以下の手順により、Aspose.Cells APIを使用してHello Worldアプリケーションを作成できます:

1. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスのインスタンスを作成します。
1. ライセンスをお持ちの場合は、[適用します](/cells/ja/cpp/licensing/)。
   評価版を使用している場合は、ライセンスに関連するコード行をスキップします。
1. Excelファイルのワークシートの任意のセルにアクセスします。
1. セルに "**Hello World!**" という単語を挿入します。
1. 変更されたMicrosoft Excelファイルを生成します。

上記の手順の実装は、以下の例で示されています。

### **コードサンプル: 新しいワークブックの作成**

次の例では、新しいブックをゼロから作成し、最初のワークシートのセルA1に "**Hello World!**" を挿入し、Excelファイルを保存します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

### **コードサンプル: 既存のファイルを開く**

次の例では、既存のMicrosoft Excelテンプレートファイルを開き、セルA1の値を取得してチェックします。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
