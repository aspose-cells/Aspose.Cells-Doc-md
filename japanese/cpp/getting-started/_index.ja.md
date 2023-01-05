---
title: 入門
type: docs
weight: 10
url: /ja/cpp/getting-started/
description: Aspose Cells for C++ をインストールして Hello World アプリケーションを作成する方法。
---
{{% alert color="primary" %}} 

このページでは、Aspose Cells for C++ をインストールして Hello World アプリケーションを作成する方法を説明します。

{{% /alert %}}

## **インストール**

### **Aspose Cells から NuGet をインストールします**

NuGet は、Aspose.Cells for C++ をダウンロードしてインストールする最も簡単な方法です。
1. Microsoft Visual Studio プロジェクト for C++ を作成します。
2. ヘッダー ファイル「Aspose.Cells.h」をインクルードします。
3. Microsoft Visual Studio と NuGet パッケージ マネージャーを開きます。
4. 「aspose.cells.cpp」を検索して、目的の Aspose.Cells for C++ を見つけます。
5. [インストール] をクリックすると、Aspose.Cells for C++ がダウンロードされ、プロジェクトで参照されます。

**![インストール Aspose Cells から NuGet](InstallThroughNuget.png)**

 aspose.cells の nuget Web ページからダウンロードすることもできます。
[Aspose.Cells for C++ NuGet パッケージ](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[詳細については、さらに手順を実行してください](/cells/ja/cpp/installation/)

### **Windows で Aspose.Cells for C++ を使用するためのデモ**

1. 次のページから Aspose.Cells for C++ をダウンロードします。
[ダウンロード Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. パッケージを解凍すると、Aspose.Cells for C++ の使用方法に関するデモが見つかります。
3. Visual Studio 2017 以降のバージョンで Demo.sln を開きます
4. main.cpp: このファイルは、Aspose.Cells for C++ をテストするためのコーディング方法を示しています。
 5. sourceFile/resultFile: これら 2 つのフォルダーは、main.cpp で使用されるストレージ ディレクトリです。

### **Linux OS で Aspose.Cells for C++ を使用する方法**

1. 次のページから Aspose.Cells for C++ をダウンロードします。
[ダウンロード Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. パッケージを解凍すると、Linux で Aspose.Cells for C++ を使用する方法に関するデモが見つかります。
3. Linux コマンド ラインで「cd Demo」を実行します。
4. 「rm -rf build;mkdir build;cd build」を実行します
5. 「cmake ..」を実行すると、Demo フォルダに CMakeLists.txt で Makefile が作成されます
6.「make」を実行してコンパイルします
7. 「./demo」を実行すると、結果が表示されます

## **Hello World アプリケーションの作成**

以下の手順では、Aspose.Cells API を使用して Hello World アプリケーションを作成します。

1. のインスタンスを作成します[ワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラス。
1. 免許をお持ちの方は、[それを適用する](/cells/ja/cpp/licensing/).
評価版を使用している場合は、ライセンス関連のコード行をスキップしてください。
1. Excel ファイル内のワークシートの目的のセルにアクセスします。
1. "という言葉を挿入します。**Hello World!**" アクセスされたセルに。
1. 変更された Microsoft Excel ファイルを生成します。

上記の手順の実装は、以下の例で示されています。

### **コード サンプル: 新しいワークブックの作成**

次の例では、新しいワークブックを最初から作成し、"**Hello World!**" を最初のワークシートのセル A1 に入力し、Excel ファイルを保存します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1.cpp" >}}

### **コード サンプル: 既存のファイルを開く**

次の例では、既存の Microsoft Excel テンプレート ファイルを開き、セルを取得して、セル A1 の値を確認します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1.cpp" >}}
