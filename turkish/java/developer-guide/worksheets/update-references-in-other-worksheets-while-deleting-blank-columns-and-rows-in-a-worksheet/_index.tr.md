---
title: Bir çalışma sayfasındaki boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelleyin
type: docs
weight: 700
url: /tr/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}} 

 Bir çalışma sayfasındaki boş sütunları ve satırları sildiğinizde, diğer çalışma sayfalarındaki referansları geçersiz olur. Bu davranıştan kaçınmak ve bu referansların da güncellenmesini istiyorsanız, lütfen[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) ve ayarla**doğru**.

{{% /alert %}} 
## **Bir çalışma sayfasındaki boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelleyin**
 Lütfen aşağıdaki örnek koda ve konsol çıktısına bakın. İkinci çalışma sayfasındaki E3 hücresi, birinci çalışma sayfasındaki C3 hücresine atıfta bulunan =Sayfa1!C3 formülüne sahiptir. eğer ayarlayacaksan[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) olarak mülkiyet**doğru** , bu formül güncellenecek ve ilk çalışma sayfasındaki boş sütunlar ve satırlar silindiğinde =Sayfa1!A1 olacaktır. Ancak, ayarlayacaksanız[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) olarak mülkiyet**YANLIŞ**, ikinci çalışma sayfasının E3 hücresindeki formül =Sayfa1!C3 olarak kalacak ve geçersiz olacaktır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Konsol Çıkışı**
Bu, yukarıdaki örnek kodun konsol çıktısıdır.[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) özellik olarak ayarlandı**doğru**.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Bu, yukarıdaki örnek kodun konsol çıktısıdır.[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) özellik olarak ayarlandı**YANLIŞ**. Gördüğünüz gibi, ikinci çalışma sayfasının E3 hücresindeki formül güncellenmedi ve hücre değeri artık 4 yerine geçersiz olan 0 oldu.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
