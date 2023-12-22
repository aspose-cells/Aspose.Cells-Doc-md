---
title: はじめる
type: docs
weight: 10
url: /ja/cpp/getting-started/
description: Aspose Cells for C++ をインストールして Hello World アプリケーションを作成する方法。
---
{{% alert color="primary" %}} 

このページでは、Aspose Cells for C++ をインストールし、Hello World アプリケーションを作成する方法を説明します。

{{% /alert %}}

##  **インストール**

###  **Aspose Cells ～ NuGet をインストールします**

NuGet は、Aspose.Cells for C++ をダウンロードしてインストールする最も簡単な方法です。
1. Microsoft Visual Studio プロジェクト for C++ を作成します。
2. ヘッダーファイル「Aspose.Cells.h」をインクルードします。
3. Microsoft Visual Studio および NuGet パッケージ マネージャーを開きます。
 4. 「aspose.cells.cpp」を検索して、目的の Aspose.Cells for C++ を見つけます。
5. [インストール] をクリックすると、Aspose.Cells for C++ がダウンロードされ、プロジェクトで参照されます。

**![Aspose Cells ～ NuGet をインストール](InstallThroughNuget.png)**

 aspose.cells の Web ページ nuget からダウンロードすることもできます。
[Aspose.Cells for C++ NuGet パッケージ](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[詳細については、さらなるステップをご覧ください](/cells/ja/cpp/installation/)

###  **Windows で Aspose.Cells for C++ を使用するためのデモ**

1. 次のページから Aspose.Cells for C++ をダウンロードします。
[ダウンロード Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. パッケージを解凍すると、Aspose.Cells for C++ の使用例が表示されます。
3. Visual Studio 2017 以降のバージョンで example.sln を開きます。
4. main.cpp: このファイルは、Aspose.Cells for C++ をテストするコードの作成方法を示しています。

###  **Linux で Aspose.Cells for C++ を使用するためのデモ**

1. 次のページから Aspose.Cells for C++ をダウンロードします。
[ダウンロード Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. パッケージを解凍すると、Linux で Aspose.Cells for C++ を使用する方法の例が見つかります。
3. サンプルが配置されているパスにいることを確認します。
4.「cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release」を実行します。
5.「cmake --build example/build」を実行します。

###  **Mac OS で Aspose.Cells for C++ を使用するためのデモ**

1. 次のページから Aspose.Cells for C++ をダウンロードします。
[ダウンロード Aspose.Cells for C++(MacOS)](https://downloads.aspose.com/cells/cpp/)
2. パッケージを解凍すると、MacOS で Aspose.Cells for C++ を使用する方法の例が見つかります。
3. サンプルが配置されているパスにいることを確認します。
4.「cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release」を実行します。
5.「cmake --build example/build」を実行します。

##  **Hello World アプリケーションの作成**

以下の手順では、Aspose.Cells API を使用して Hello World アプリケーションを作成します。

1. のインスタンスを作成します。[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラス。
1. 免許をお持ちであれば、[それを適用してください](/cells/ja/cpp/licensing/).
評価版を使用している場合は、ライセンス関連のコード行をスキップしてください。
1. Excel ファイル内のワークシートの任意のセルにアクセスします。
1. アクセスしたセルに「**Hello World!**」という単語を挿入します。
1. 変更した Microsoft Excel ファイルを生成します。

上記のステップの実装を以下の例で示します。

###  **コードサンプル: 新しいワークブックの作成**

次の例では、新しいブックを最初から作成し、最初のワークシートのセル A1 に「**Hello World!**」を挿入し、Excel ファイルを保存します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

###  **コードサンプル: 既存のファイルを開く**

次の例では、既存の Microsoft Excel テンプレート ファイルを開き、セルを取得してセル A1 の値を確認します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
