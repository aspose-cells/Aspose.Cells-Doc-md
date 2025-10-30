---
title: Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle
type: docs
weight: 5000
url: /tr/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Bu makale, Aspose.Cells for Python via .NET API tarafından bir Çalışma Sayfası ndaki boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansların nasıl güncelleneceğini göstermektedir.
keywords: Python Excel Kütüphanesi, Python da boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelleme, Python da bir Çalışma Sayfasındaki boş sütunları ve satırları silerken referansları güncelleme.
---

{{% alert color="primary" %}}

Çalışma sayfasında boş sütunları ve satırları sildiğinizde, diğer çalışma sayfalarındaki bu sütunların referansları geçersiz hale gelir. Bu davranışı önlemek ve diğer çalışma sayfalarındaki bu çalışma sayfasının referanslarının güncellenmesini istiyorsanız, lütfen [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) özelliğini kullanın ve bunu **true** olarak ayarlayın.

{{% /alert %}}

## **Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle**

Lütfen aşağıdaki örnek kodu ve konsol çıktısını inceleyin. İkinci çalışma sayfasındaki E3 hücresinde, birinci çalışma sayfasındaki C3 hücresine atıfta bulunan =Sheet1!C3 formülü bulunmaktadır. [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) özelliğini **true** olarak ayarlarsanız, bu formülü sildiğinizde güncellenecek ve birinci çalışma sayfasında boş sütunları ve satırları sildiğinizde =Sheet1!A1 olacaktır. Ancak [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) özelliğini **false** olarak ayarlarsanız, ikinci çalışma sayfasındaki formül =Sheet1!C3 olmaya devam eder ve geçersiz hale gelir.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-UpdateReferenceInWorksheets.py" >}}

### **Konsol Çıktısı**

[**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) özelliği **true** olarak ayarlandığında yukarıdaki örnek kodun konsol çıktısı budur.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

[**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) özelliği **false** olarak ayarlandığında yukarıdaki örnek kodun konsol çıktısı budur. Görebileceğiniz gibi, ikinci çalışma sayfasındaki formül güncellenmedi ve hücre değeri artık geçersizdir ve 0'dır.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
