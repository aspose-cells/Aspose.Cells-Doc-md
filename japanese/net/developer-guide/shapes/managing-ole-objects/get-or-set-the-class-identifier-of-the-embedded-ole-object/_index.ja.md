---
title: 埋め込みOLEオブジェクトのクラス識別子を取得または設定する
type: docs
weight: 200
url: /ja/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **可能な使用シナリオ**
Aspose.Cellsは、[OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)プロパティを提供し、埋め込まれたOLEオブジェクトのクラス識別子を取得または設定できます。OLEオブジェクトクラス識別子は実際にはGUID、すなわちグローバル固有識別子です。GUIDは常に16バイトの長さであり、クラス識別子も16バイトの長さです。それらはWindowsレジストリ内によく見られ、クライアントアプリケーション内のさまざまな埋め込まれたリソースを含むOLEオブジェクトを開くための情報を提供します。
## **埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する**
以下のスクリーンショットは、埋め込まれたPowerPoint OLEオブジェクトを含む[サンプルExcelファイル](5115190.xls)から読み取られたOLEオブジェクトクラス識別子であるGUIDを示しています。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **サンプルコード**
以下のサンプルコードは、[サンプルExcelファイル](5115190.xls)とそのコンソール出力で実行され、OLEオブジェクトのクラス識別子であるGUIDを出力します。出力されたGUIDは、スクリーンショット内で示されているものとまったく同じです。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **コンソール出力**
上記のサンプルコードを[サンプルExcelファイル](5115190.xls)で実行した場合のコンソール出力です。

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
