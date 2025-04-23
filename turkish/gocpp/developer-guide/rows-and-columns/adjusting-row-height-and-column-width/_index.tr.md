---
title: Satır Yüksekliğini ve Sütun Genişliğini Ayarlama
type: docs
weight: 10
url: /tr/go-cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}}

Yayınlanan veri tabloları üzerinde çalışırken, satırlara veya sütunlara veri eklerken, bazen satırların yüksekliğini veya sütunların genişliğini değiştirmeniz gerekebilir. Bazen satırlara veya sütunlara biçimlendirme uygulamak, mevcut yükseklik veya genişliğin veriyi gösterebilecek şekilde değişmesi gerektiği anlamına gelir. Genellikle, kullanıcılar satır yüksekliklerini ve sütun genişliklerini Microsoft Excel kullanarak WYSIWYG ortamında ayarlar. Ancak, Aspose.Cells geliştiricileri bu işlemleri çalışma zamanında gerçekleştirebilirler.

{{% /alert %}}

## **Satırlarla Çalışmak**

### **Satır Yüksekliğini Ayarlamak**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, her çalışma sayfasına erişimi sağlayan [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı, tüm hücreleri temsil eden [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonu sağlar. Bu koleksiyon, satır veya sütunları yönetmek için çeşitli yöntemler içerir.

#### **Bir Satırın Yüksekliğini Ayarlama**

Belirli bir satır yüksekliğini ayarlamak için, [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) yöntemini çağırabilirsiniz. [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) yöntemi aşağıdaki parametreleri alır:

- **Satır dizini**, yüksekliği değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanan satır yüksekliği.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-GPP-SettingHeightOfRow.go" >}}

#### **Bir Çalışma Sayfasındaki Tüm Satırların Yüksekliğini Ayarlama**

Eğer geliştiriciler tüm satırlarda aynı satır yüksekliğini ayarlamak isterse, bunu [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [SetStandardHeight](https://reference.aspose.com/cells/go-cpp/cells/setstandardheight/) yöntemi kullanarak yapabilirler.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingHeightOfAllRowsInWorksheet.go" >}}

## **Sütunlarla Çalışmak**

### **Bir Sütunun Genişliğini Ayarlamak**

Bir sütunun genişliğini ayarlamak için, [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) yöntemini çağırabilirsiniz. [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) yöntemi aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliği değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfColumn.go" >}}

### **Bir Çalışma Sayfasındaki Tüm Sütunların Genişliğini Ayarlama**

Tüm satırlara aynı sütun genişliğini ayarlamak için, [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [SetStandardWidth](https://reference.aspose.com/cells/go-cpp/cells/setstandardwidth/) yöntemini kullanın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfAllColumnsInWorksheet.go" >}}
