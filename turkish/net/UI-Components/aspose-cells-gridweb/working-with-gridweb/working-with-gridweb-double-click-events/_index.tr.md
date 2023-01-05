---
title: GridWeb Çift Tıklama Olaylarıyla Çalışma
type: docs
weight: 80
url: /tr/net/working-with-gridweb-double-click-events/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb üç tür çift tıklama olayı içerir:

- CellDoubleClick, bir hücre çift tıklandığında tetiklenir.
- ColumnDoubleClick, bir sütun başlığına çift tıklandığında tetiklenir.
- RowDoubleClick, bir satır başlığına çift tıklandığında tetiklenir.

Bu konuda, Aspose.Cells.GridWeb'de çift tıklama olaylarının nasıl etkinleştirileceği anlatılmaktadır. Ayrıca, bu olaylar için olay işleyicileri oluşturmayı da tartışır.

{{% /alert %}} 
## **Çift Tıklama Olaylarını Etkinleştirme**
GridWeb denetiminin EnableDoubleClickEvent özelliği true olarak ayarlanarak, tüm çift tıklama olayları istemci tarafında etkinleştirilebilir.

{{% alert color="primary" %}} 

Varsayılan olarak, EnableDoubleClickEvent özelliği false olarak ayarlanır. Bu, çift tıklama olaylarının varsayılan olarak etkin olmadığı anlamına gelir. Bu tür olayları uygulamak için önce özelliği etkinleştirin.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



Çift tıklama olayları etkinleştirildiğinde, herhangi bir çift tıklama olayı için olay işleyicileri oluşturmak mümkündür. Bu olay işleyicileri, belirli bir çift tıklama olayı başlatıldığında belirli görevleri gerçekleştirir.
## **Çift Tıklama Olaylarını Yönetme**
Visual Studio'da bir olay işleyicisi oluşturmak için:

1.  içindeki bir olayı çift tıklatın.**Olaylar** Özellikler bölmesindeki liste.

Bu örnek için, çeşitli çift tıklama olayları için olay işleyicileri uyguladık.
### **Çift Tık Cell**
CellDoubleClick olayı için olay işleyicisi, çift tıklanan hücrenin tüm bilgilerini sağlayan CellEventArgs türünde bir bağımsız değişken sağlar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Sütun Başlığına Çift Tıklama**
ColumnDoubleClick olayı için olay işleyicisi, çift tıklanan başlık için sütunun dizin numarasını ve diğer bilgileri sağlayan RowColumnEventArgs türünde bir bağımsız değişken sağlar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Satır Başlığına Çift Tıklama**
RowDoubleClick olayı için olay işleyicisi, çift tıklanan başlık için satırın dizin numarasını ve diğer ilgili bilgileri sağlayan RowColumnEventArgs türünde bir bağımsız değişken sağlar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
