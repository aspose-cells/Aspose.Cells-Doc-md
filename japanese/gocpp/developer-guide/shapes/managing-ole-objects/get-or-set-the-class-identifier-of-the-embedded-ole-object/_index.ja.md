---
title: Go言語を使用してC++経由で埋め込みOLEオブジェクトのクラス識別子を取得または設定する
linktitle: 埋め込みOLEオブジェクトのクラス識別子を取得または設定する
type: docs
weight: 200
url: /ja/go-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: C++を経由してGo言語とAspose.Cellsを使った埋め込みOLEオブジェクトのクラス識別子の取得または設定方法を学びます。
---

## **可能な使用シナリオ**
Aspose.Cellsは[OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/go-cpp/oleobject/getclassidentifier/)プロパティを提供し、埋め込みOLEオブジェクトのクラス識別子の取得または設定に使用できます。OLEオブジェクトのクラス識別子は実際にはGUID（グローバル一意識別子）です。GUIDは常に16バイト長であり、クラス識別子も16バイト長です。これらはWindowsレジストリ内で見つかることが多く、クライアントアプリケーション内のさまざまな埋め込みリソースを含む埋め込みOLEオブジェクトの開き方に関する情報をホストアプリケーションに提供します。

## **埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する**
以下のスクリーンショットは、[サンプルエクセルファイル](5115190.xls)から読み取られたOLEオブジェクトのクラス識別子（GUID）を示しています。これは埋め込みPowerPoint OLEオブジェクトを含んでいます。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **サンプルコード**
次のサンプルコードは、[サンプルエクセルファイル](5115190.xls)とともに実行され、OLEオブジェクトのクラス識別子（GUID）をコンソールに出力します。出力されるGUIDはスクリーンショットに表示されているものと全く同じです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetOrSetTheClassIdentifierOfTheEmbeddedOleObject.go" >}}
### **コンソール出力**
上記のサンプルコードを[サンプルExcelファイル](5115190.xls)で実行した場合のコンソール出力です。

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
