---
title: Phpでのページ休憩の管理
type: docs
weight: 20
url: /ja/java/managing-page-breaks-in-php/
---

## **Aspose.Cells - ページの区切りを管理する**
### **ページブレークの追加**
**Aspose.Cells Java for PHP**を使用してページ休憩を追加するには、**pagebreaks**モジュールの**add_page_breaks**メソッドを呼び出します。以下にコード例を示します。

**PHPコード**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->add("Y30");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Add Page Breaks.xls");   

{{< /highlight >}}
### **すべてのページの改ページをクリアする**
**Aspose.Cells Java for PHP**を使用して、すべてのページ休憩をクリアするには、**pagebreaks**モジュールの**clear_all_page_breaks**メソッドを呼び出します。以下にコード例を示します。

**PHPコード**

{{< highlight php >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **特定の改ページを削除する**
**Aspose.Cells Java for PHP**を使用して特定の改ページを削除するには、**pagebreaks**モジュールの**remove_page_break**メソッドを呼び出します。以下にコード例が示されています。

**PHPコード**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->removeAt(0);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Remove Page Break.xls");

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから**Managing Page Breaks (Aspose.Cells)**をダウンロードしてください。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
