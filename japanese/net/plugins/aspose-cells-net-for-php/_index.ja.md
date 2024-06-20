---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /ja/net/aspose-cells-net-for-php/
---

## **はじめに**

### **紹介**

### **システム要件およびサポートされるプラットフォーム**

#### **システム要件**

**Aspose.Cells .NET for PHPを使用するためのシステム要件は次のとおりです:**

- PHPとPHP ManagerがインストールされたIIS。
- Aspose.Total APIs.
- Aspose.CellsのInterop dllとtlbファイル。

#### **サポートされているプラットフォーム**

**サポートされているプラットフォームは次のとおりです:**

- PHP 5.3以上
- Windows OS

### **ダウンロードと構成**

#### **必要なライブラリのダウンロード**

以下に記載されている必須ライブラリをダウンロードしてください。これらはAspose.Cells Java for PHPの例の実行に必要です。

- [ダウンロード Aspose.Cells for .NET (DLLまたはMSI) ファイルをダウンロードセクションから](https://downloads.aspose.com/cells/net)
- [Aspose.Cells for .NETインタープオープdllのダウンロード](https://downloads.aspose.com/cells/net)

MSIバージョンをダウンロードすると、デフォルトでインストールされた場所にAspose.Cells.dllをC：\ Program Files（x86）\ Aspose\ Aspose.Cells for .NET\ Bin\ net2.0フォルダに見つけることができます。
ただし、DLLバージョンをダウンロードした場合は、それを展開して、Aspose.Cells.dllを.NET 2.0フォルダからc：\ tempフォルダにコピーして使用しやすくすることができます。
同様に、Interopzipファイルを抽出し、Aspose.Inteop.dllをc：\ tempにコピーします

#### **ソーシャルコーディングサイトから例をダウンロードする**

実行中の例のリリースは、以下に記載されているソーシャルコーディングサイトでダウンロードできます：

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Examples**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Windowsプラットフォームでのソースコードの構成方法**

次のシンプルな手順に従ってソースコードを開いて拡張する方法を見ていきます

##### **1. Aspose.Cells.dllおよびAspose.Cells.Interop.dllなどのdllおよびinterop.dllファイルを登録します。**

{{< highlight java >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. PHPでCOMおよびDOTNET拡張機能を有効にします。**

IISでPHPマネージャを開き、「有効または無効にする拡張機能」をクリックします。 php_com_dotnet.dllを見つけ、有効になっていることを確認してください。

##### **3. Aspose.Cells .NET for PHPの例を構成する**

###### **方法1**

[github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)からPHPの例をクローンします
次のコマンドを実行します

{{< highlight java >}}

 composer install

{{< /highlight >}}

###### **方法2**

PHPプロジェクトのcomposer.jsonファイルに次の行を追加します

{{< highlight java >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

次のインストールコマンドを実行します

{{< highlight java >}}

 composer install

{{< /highlight >}}

To read about composer visit <https://getcomposer.org/>

### **拡張と貢献をサポートする**

#### **サポート**

Asposeが立ち上がって最初の日から、良い製品だけを提供するだけでは不十分だと分かっていました。良いサービスも提供する必要がありました。私たち自身も開発者であり、技術的な問題やソフトウェアの不具合が必要なことを妨げるときにどれだけイライラするか理解しています。私たちは問題を解決するためにここにいて、それを作り出すためではありません。

そのため、無料サポートを提供しています。製品を購入したか、評価を使用しているかに関わらず、私たちの製品を使用するすべての人にフルの注意と尊敬を提供する価値があります。

Aspose.Cells .NET for PHPに関連する問題や提案を以下のいずれかのプラットフォームを使用してログに記録できます：

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **拡張と貢献**

Aspose.Cells .NET for PHPはオープンソースであり、そのソースコードは以下にリストされている主要なソーシャルコーディングウェブサイトで利用できます。 開発者はソースコードをダウンロードし、新機能の提案や追加、または既存の機能の改善を行うことを奨励されています。他の人々もそれを利用できるように。

#### **ソースコード**

最新のソースコードを以下の場所から取得できます

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **サンプルコード例**

このセクションには以下のトピックが含まれています

- [PHPプログラマーズガイド](/cells/ja/net/php-programmers-guide/)
  - [PHPでファイルを操作する](/cells/ja/net/working-with-files-in-php/)
    - [PHPのファイル処理機能](/cells/ja/net/file-handling-features-in-php/)
      - [PHPでファイルを開く](/cells/ja/net/opening-files-in-php/)
      - [PHPでファイルを保存](/cells/ja/net/saving-files-in-php/)
    - [PHPでのユーティリティ機能](/cells/ja/net/utility-features-in-php/)
      - [PHPでファイルを暗号化](/cells/ja/net/encrypting-files-in-php/)
      - [PHPでExcelからPDFへの変換](/cells/ja/net/excel-to-pdf-conversion-in-php/)
      - [PHPでドキュメントプロパティを管理する](/cells/ja/net/managing-document-properties-in-php/)
      - [PHPでワークシートを画像に変換する](/cells/ja/net/worksheet-to-image-conversion-in-php/)
  - [PHPでの数式の処理](/cells/ja/net/working-with-formulas-in-php/)
    - [PHP で数式を計算する](/cells/ja/net/calculating-formulas-in-php/)
  - [PHP でワークシートを操作する](/cells/ja/net/working-with-worksheets-in-php/)
    - [PHP での管理機能](/cells/ja/net/management-features-in-php/)
      - [PHP でワークシートを管理する](/cells/ja/net/managing-worksheets-in-php/)
        - [PHP で既存のExcelファイルにワークシートを追加する](/cells/ja/net/add-worksheets-to-existing-excel-file-in-php/)
        - [PHP で新しいExcelファイルにワークシートを追加する](/cells/ja/net/add-worksheets-to-new-excel-file-in-php/)
        - [PHP でシートインデックスを使用してワークシートを削除する](/cells/ja/net/removing-worksheets-using-sheet-index-in-php/)
        - [PHP でシート名を使用してワークシートを削除する](/cells/ja/net/removing-worksheets-using-sheet-name-in-php/)
