---
title: Bir çalışma sayfasındaki boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelleyin
type: docs
weight: 5000
url: /tr/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}}

Bir çalışma sayfasındaki boş sütunları ve satırları sildiğinizde, diğer çalışma sayfalarındaki referansları geçersiz olur. Bu davranıştan kaçınmak ve mevcut çalışma sayfasının diğer çalışma sayfalarındaki referanslarının da güncellenmesini istiyorsanız, lütfen[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) özellik ve bunu ayarlayın**doğru**.

{{% /alert %}}

## **Bir çalışma sayfasındaki boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelleyin**

 Lütfen aşağıdaki örnek koda ve konsol çıktısına bakın. İkinci çalışma sayfasındaki E3 hücresi, birinci çalışma sayfasındaki C3 hücresine atıfta bulunan =Sayfa1!C3 formülüne sahiptir. eğer ayarlayacaksan[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) olarak mülkiyet**doğru** , bu formül güncellenecek ve ilk çalışma sayfasındaki boş sütunlar ve satırlar silindiğinde =Sayfa1!A1 olacaktır. Ancak, ayarlayacaksanız[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) olarak mülkiyet**yanlış**, ikinci çalışma sayfasının E3 hücresindeki formül =Sayfa1!C3 olarak kalacak ve geçersiz olacaktır.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Konsol Çıkışı**

 Bu, yukarıdaki örnek kodun konsol çıktısıdır.[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) özellik olarak ayarlandı**doğru**.

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

 Bu, yukarıdaki örnek kodun konsol çıktısıdır.[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) özellik olarak ayarlandı**yanlış**. Gördüğünüz gibi, ikinci çalışma sayfasının E3 hücresindeki formül güncellenmedi ve hücre değeri artık 4 yerine geçersiz olan 0 oldu.

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
