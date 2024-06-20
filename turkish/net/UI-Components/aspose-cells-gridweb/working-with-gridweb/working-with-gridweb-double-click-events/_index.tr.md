---
title: GridWeb Çift Tıklayın Olayları ile Çalışma
type: docs
weight: 80
url: /tr/net/aspose-cells-gridweb/gridweb-double-click-event/
keywords: GridWeb, çift tıklayın, tıklayın olayı, olay
description: Bu makale, GridWeb de çift tıklama olayının nasıl kullanılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, üç tür çift tıklama olayı içerir:

- CellDoubleClick, bir hücre çift tıklandığında tetiklenir.
- ColumnDoubleClick, bir sütun başlığı çift tıklandığında tetiklenir.
- RowDoubleClick, bir satır başlığı çift tıklandığında tetiklenir.

Bu konu, Aspose.Cells.GridWeb'de çift tıklama olaylarını etkinleştirmeyi ve bu olaylar için olay işleyicileri oluşturmayı tartışmaktadır.

{{% /alert %}} 
## **Çift Tıklama Olaylarını Etkinleştirme**
Tüm çift tıklama olayları, GridWeb kontrolünün EnableDoubleClickEvent özelliğinin true olarak ayarlanmasıyla istemci tarafında etkinleştirilebilir.

{{% alert color="primary" %}} 

EnableDoubleClickEvent özelliği varsayılan olarak false olarak ayarlanmıştır. Bu, çift tıklama olaylarının varsayılan olarak etkin olmadığı anlamına gelir. Bu tür olayları uygulamak için önce özelliği etkinleştirmeniz gerekir.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



Çift tıklama olayları etkinleştirildiğinde, herhangi bir çift tıklama olayı için olay işleyicileri oluşturmak mümkündür. Bu olay işleyicileri, belirli bir çift tıklama olayı tetiklendiğinde belirli görevleri gerçekleştirir.
## **Çift Tıklama Olaylarını Ele Almak**
Visual Studio'da bir olay işleyici oluşturmak için:

1. Özellikler bölmesindeki Olaylar listesinde bir olaya çift tıklayın.

Bu örnekte, çeşitli çift tıklama olayları için olay işleyicileri uyguladık.
### **Hücreyi Çift Tıklama**
CellDoubleClick olay işleyicisi, çift tıklanan hücre ile ilgili tam bilgiyi sağlayan CellEventArgs türünden bir argüman sağlar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Sütun Başlığını Çift Tıklama**
ColumnDoubleClick olay işleyicisi, çift tıklanan başlık için sütunun indeks numarasını ve diğer bilgileri sağlayan RowColumnEventArgs türünden bir argüman sağlar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Satır Başlığını Çift Tıklama**
RowDoubleClick olay işleyicisi, çift tıklanan başlık için satırın indeks numarasını ve diğer ilgili bilgileri sağlayan RowColumnEventArgs türünden bir argüman sağlar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
