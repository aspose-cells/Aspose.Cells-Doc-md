---
title: Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle
type: docs
weight: 5000
url: /tr/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}}

Çalışma sayfasında boş sütunları ve satırları sildiğinizde, diğer çalışma sayfalarındaki bu sütunların referansları geçersiz hale gelir. Bu davranışı önlemek ve diğer çalışma sayfalarındaki bu çalışma sayfasının referanslarının güncellenmesini istiyorsanız, lütfen [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) özelliğini kullanın ve bunu **true** olarak ayarlayın.

{{% /alert %}}

## **Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle**

Lütfen aşağıdaki örnek kodu ve konsol çıktısını inceleyin. İkinci çalışma sayfasındaki E3 hücresinde, birinci çalışma sayfasındaki C3 hücresine atıfta bulunan =Sheet1!C3 formülü bulunmaktadır. [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) özelliğini **true** olarak ayarlarsanız, bu formülü sildiğinizde güncellenecek ve birinci çalışma sayfasında boş sütunları ve satırları sildiğinizde =Sheet1!A1 olacaktır. Ancak [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) özelliğini **false** olarak ayarlarsanız, ikinci çalışma sayfasındaki formül =Sheet1!C3 olmaya devam eder ve geçersiz hale gelir.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Konsol Çıktısı**

[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) özelliği **true** olarak ayarlandığında yukarıdaki örnek kodun konsol çıktısı budur.

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

[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) özelliği **false** olarak ayarlandığında yukarıdaki örnek kodun konsol çıktısı budur. Görebileceğiniz gibi, ikinci çalışma sayfasındaki formül güncellenmedi ve hücre değeri artık geçersizdir ve 0'dır.

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
