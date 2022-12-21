---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /ja/net/aspose-cells-net-for-php/
---
## **入門**

### **序章**

### **システム要件とサポートされるプラットフォーム**

#### **システム要求**

**Aspose.Cells .NET for PHP を使用するためのシステム要件は次のとおりです。**

- PHP と PHP Manager がインストールされた IIS。
- Aspose.Total API。
- Aspose.Cells Interop dll および tlb ファイル。

#### **サポートされているプラットフォーム**

**サポートされているプラットフォームは次のとおりです。**

- PHP 5.3 以上
- Windows OS

### **ダウンロードと構成**

#### **必要なライブラリをダウンロード**

下記の必要なライブラリをダウンロードします。これらは、Aspose.Cells Java for PHP の例を実行するために必要です。

- [ダウンロード セクションから Aspose.Cells for .NET (DLL または MSI) ファイルをダウンロードします。](https://downloads.aspose.com/cells/net)
- [Aspose.Cells for .NET 相互運用 dll をダウンロード](https://downloads.aspose.com/cells/net)

MSI バージョンをダウンロードすると、デフォルトでは C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0 フォルダーに Aspose.Cells.dll が見つかります。
ただし、DLL バージョンをダウンロードした場合は、それを抽出し、使いやすいように .NET 2.0 フォルダーから Aspose.Cells.dll を c:\temp フォルダーにコピーできます。
同様に、interop zip ファイルを抽出し、Aspose.Inteop.dll を c:\temp にコピーします。

#### **ソーシャル コーディング サイトからサンプルをダウンロードする**

実行中のサンプルの次のリリースは、以下のソーシャル コーディング サイトからダウンロードできます。

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP 例**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Windows プラットフォームでのソース コードの設定方法**

使用中にソース コードを開いて拡張するには、次の簡単な手順に従ってください。

##### **1. dll ファイルと interop.dll ファイルの両方を登録します (例: Aspose.Cells.dll と Aspose.Cells.Interop.dll)。**

{{< highlight "java" >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. PHP で COM および DOTNET 拡張機能を有効にします。**

IIS で PHP マネージャーを開き、[有効にして無効にして拡張] をクリックします。 PHPを探す_コム_dotnet.dll を開き、有効になっていることを確認します。

##### **3. Aspose.Cells .NET for PHP の例を設定します。**

###### **方法 1**

からPHPの例をクローン[ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
次のコマンドを実行します

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

###### **方法 2**

PHP プロジェクトの composer.json ファイルに次の行を追加します。

{{< highlight "java" >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

インストールコマンドを実行します

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

作曲家の訪問について読むには<https://getcomposer.org/>

### **サポート拡張と貢献**

#### **サポート**

Aspose の最初の日から、私たちはお客様に良い製品を提供するだけでは十分ではないことを知っていました。また、優れたサービスを提供する必要もありました。私たち自身も開発者であり、技術的な問題やソフトウェアの異常によって必要な作業ができなくなると、どれほどイライラするかを理解しています。問題を作成するのではなく、問題を解決するためにここにいます。

そのため、無料サポートを提供しています。私たちの製品を購入したか、評価を使用しているかにかかわらず、私たちの製品を使用するすべての人は、私たちの十分な注意と尊敬に値します.

次のプラットフォームのいずれかを使用して、Aspose.Cells .NET for PHP に関連する問題や提案を記録できます。

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **拡張して貢献する**

Aspose.Cells .NET for PHP はオープン ソースであり、そのソース コードは、以下に示す主要なソーシャル コーディング Web サイトで入手できます。開発者は、ソース コードをダウンロードし、新しい機能を提案または追加するか、既存の機能を改善することによって貢献することをお勧めします。これにより、他の人もその恩恵を受けることができます。

#### **ソースコード**

最新のソース コードは、次のいずれかの場所から入手できます。

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **サンプルコードの例**

このセクションには、次のトピックが含まれています

- [PHP プログラマー ガイド](/cells/ja/net/php-programmers-guide/)
  - [PHP でのファイルの操作](/cells/ja/net/working-with-files-in-php/)
    - [PHP のファイル処理機能](/cells/ja/net/file-handling-features-in-php/)
      - [PHP でファイルを開く](/cells/ja/net/opening-files-in-php/)
      - [PHP でファイルを保存する](/cells/ja/net/saving-files-in-php/)
    - [PHP のユーティリティ機能](/cells/ja/net/utility-features-in-php/)
      - [PHP でのファイルの暗号化](/cells/ja/net/encrypting-files-in-php/)
      - [PHP での Excel から PDF への変換](/cells/ja/net/excel-to-pdf-conversion-in-php/)
      - [PHP でのドキュメント プロパティの管理](/cells/ja/net/managing-document-properties-in-php/)
      - [PHP でのワークシートから画像への変換](/cells/ja/net/worksheet-to-image-conversion-in-php/)
  - [PHP で数式を操作する](/cells/ja/net/working-with-formulas-in-php/)
    - [PHP で数式を計算する](/cells/ja/net/calculating-formulas-in-php/)
  - [PHP でのワークシートの操作](/cells/ja/net/working-with-worksheets-in-php/)
    - [PHP の管理機能](/cells/ja/net/management-features-in-php/)
      - [PHP でのワークシートの管理](/cells/ja/net/managing-worksheets-in-php/)
        - [PHP で既存の Excel ファイルにワークシートを追加する](/cells/ja/net/add-worksheets-to-existing-excel-file-in-php/)
        - [PHP で新しい Excel ファイルにワークシートを追加する](/cells/ja/net/add-worksheets-to-new-excel-file-in-php/)
        - [PHP でシート インデックスを使用してワークシートを削除する](/cells/ja/net/removing-worksheets-using-sheet-index-in-php/)
        - [PHP でシート名を使用してワークシートを削除する](/cells/ja/net/removing-worksheets-using-sheet-name-in-php/)
