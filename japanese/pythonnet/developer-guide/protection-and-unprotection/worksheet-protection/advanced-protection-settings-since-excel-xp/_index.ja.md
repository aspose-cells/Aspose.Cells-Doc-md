---
title: Excel XP以降の高度な保護設定
type: docs
weight: 30
url: /ja/python-net/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

Excel 2002またはXPのリリース以降、Microsoftは多くの高度な保護設定を追加しました。

{{% /alert %}}

## **紹介**

これらの保護設定により、ユーザーは次の操作を制限または許可できます：

- 行または列の削除。
- 内容、オブジェクト、またはシナリオの編集。
- セル、行、または列の書式設定。
- 行、列、またはハイパーリンクの挿入。
- ロックされたセルまたはロックされていないセルの選択。
- ピボットテーブルなどの使用。

Aspose.Cells for Python via .NETは、Excel XP以降のすべての高度な保護設定をサポートしています。

### **Excel XPおよびそれ以降のバージョンを使用した高度な保護設定**

Excel XPで利用可能な保護設定を表示するには：

1. **ツール**メニューから、**保護**の後に**シートを保護**を選択します。ダイアログが表示されます。

Excel 2016で利用可能な保護設定を表示するには

1. **ファイル**メニューから、**ワークブックを保護**, その後**現在のシートを保護**を選択します。
1. **レビュー**メニューで**シートを保護**を選択します。

上記の手順に従うと、ワークシートの機能を許可または制限したり、ワークシートにパスワードを適用したりするダイアログが表示されます。

### **Aspose.Cells for Python via .NETを使用した高度な保護設定**

Aspose.Cells for Python via .NETは、すべての高度な保護設定をサポートしています。

Aspose.Cells for Python via .NET は、Microsoft Excelファイルを表すクラス [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) クラスは、Excelファイル内の各ワークシートにアクセスできる [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) コレクションを含みます。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスで表されます。

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは、これらの高度な保護設定を適用するために使用される[**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection)プロパティを提供します。[**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection)プロパティは実際には[**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection)クラスのオブジェクトであり、無効化または有効化するための複数のブール値プロパティをカプセル化しています。

以下は小さなサンプルアプリケーションです。それはExcelファイルを開いて、Excel XPおよびそれ以降のバージョンでサポートされる高度な保護設定のほとんどを使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AdvancedProtectionSettings-1.py" >}}

{{% alert color="primary" %}}

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**protect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect)メソッドを呼び出さないでください。また、高度な保護設定はExcel XPおよび以降のバージョンでのみサポートされているため、ファイルをExcel97To2003またはXlsx形式で保存してください。

{{% /alert %}}

### **セルロックの問題**

セルの編集を制限したい場合は、保護設定を適用する前にセルをロックする必要があります。そうでない場合、ワークシートが保護されていてもセルが編集できます。Microsoft Excel XPでは、次のダイアログでセルをロックできます:

|**Excel XPでセルをロックするダイアログ**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Aspose.Cells for Python via .NET APIを使えばセルをロックすることも可能です。各セルは [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) 形式を持ち、その中にブーリアンの属性 [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) があります。セルをロックまたはアンロックするには [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) 属性を**true**または**false**に設定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-LockCell-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
