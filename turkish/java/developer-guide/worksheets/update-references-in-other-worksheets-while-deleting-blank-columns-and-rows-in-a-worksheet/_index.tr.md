---
title: Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle
type: docs
weight: 700
url: /tr/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}} 

Bir çalışsayfadaki boş sütunları ve satırları sildiğinizde, diğer iş sayfalarındaki bu referanslar geçersiz hale gelir. Bu davranışı önlemek istiyorsanız ve bu referansların da güncellenmesini istiyorsanız, lütfen [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) kullanın ve onu **true** olarak ayarlayın.

{{% /alert %}} 
## **Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle**
Lütfen aşağıdaki örnek kodu ve konsol çıktısını inceleyin. İkinci çalışsayfadaki E3 hücresinde, birinci çalışsayfadaki C3 hücresine atıfta bulunan =Sheet1!C3 formülü bulunmaktadır. Eğer [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) özelliğini **true**olarak ayarlarsanız, bu formül güncellenecek ve ilk çalışsayfadaki boş sütunları ve satırları sildiğinizde =Sheet1!A1 olacaktır. Ancak [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) özelliğini **false** olarak ayarlarsanız, ikinci çalışsayfadaki E3 hücresindeki formül =Sheet1!C3 olarak kalacak ve geçersiz hale gelecektir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı, [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) özelliği **true** olarak ayarlandığında.

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

Yukarıdaki örnek kodun konsol çıktısı, [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) özelliği **false** olarak ayarlandığında. Görebileceğiniz gibi, ikinci çalışsayfadaki E3 hücresindeki formül güncellenmedi ve hücre değeri artık geçersiz olan 0'dır, 4 değil.

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
