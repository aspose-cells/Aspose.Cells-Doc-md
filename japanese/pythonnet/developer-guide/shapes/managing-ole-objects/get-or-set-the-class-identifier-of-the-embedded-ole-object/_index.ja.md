---
title: 埋め込みOLEオブジェクトのクラス識別子を取得または設定する
type: docs
weight: 200
url: /ja/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **可能な使用シナリオ**
Aspose.Cells for Python via .NETは、{https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/class_identifier](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/class_identifier)プロパティを提供しており、これを使用して埋め込みOLEオブジェクトのクラス識別子を取得または設定できます。OLEオブジェクトのクラス識別子は実際にはGUID（グローバル一意識別子）です。GUIDは16バイトの長さであり、クラス識別子も16バイトです。これらはしばしばWindowsレジストリ内に見つかり、ホストアプリケーションに埋め込まれたリソースを含むOLEオブジェクトを開く方法などの情報を提供します。

## **埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する**
以下のスクリーンショットは、埋め込まれたPowerPoint OLEオブジェクトを含む[サンプルExcelファイル](5115190.xls)から読み取られたOLEオブジェクトクラス識別子であるGUIDを示しています。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **サンプルコード**
以下のサンプルコードは、[サンプルExcelファイル](5115190.xls)とそのコンソール出力で実行され、OLEオブジェクトのクラス識別子であるGUIDを出力します。出力されたGUIDは、スクリーンショット内で示されているものとまったく同じです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-GetSetClassIdentifierEmbedOleObject.py" >}}

### **コンソール出力**
上記のサンプルコードを[サンプルExcelファイル](5115190.xls)で実行した場合のコンソール出力です。

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
