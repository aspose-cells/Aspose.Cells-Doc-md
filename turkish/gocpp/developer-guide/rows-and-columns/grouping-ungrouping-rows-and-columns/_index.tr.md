---
title: Gruplama, Gruplamanın Kaldırılması Satır ve Sütunlar
type: docs
weight: 30
url: /tr/go-cpp/grouping-ungrouping-rows-and-columns/
---

## **Giriş**

Bir Microsoft Excel dosyasında, veriler için bir biçim oluşturarak tek bir fare tıklamasıyla ayrıntı seviyelerini gösterip gizleyebilirsiniz.

Hızlıca sadece özet veya başlık sağlayan satırları veya sütunları veya ayrıntıları görmek için **Anahat Sembolleri** 1,2,3, + ve - düğmelerini tıklayın veya bir bireysel özet veya başlık altındaki ayrıntıları görmek için sembolleri kullanabilirsiniz.

## **Satır ve Sütunların Grup Yönetimi**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) adlı sınıfı sağlar. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, her çalıştırma sayfasına erişim sağlayan [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı, içerdiği tüm hücreleri temsil eden [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunu sağlar.

Bir çalışma sayfasındaki satır veya sütunları yönetmek için kullanılabilecek birkaç yöntem bulunmaktadır, bunlardan bazıları aşağıda daha detaylı olarak açıklanmıştır.

### **Satır ve Sütunların Gruplandırılması**

Satırları veya sütunları, [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [GroupRows](https://reference.aspose.com/cells/go-cpp/cells/grouprows/) ve [GroupColumns](https://reference.aspose.com/cells/go-cpp/cells/groupcolumns/) yöntemlerini çağırarak gruplayabilirsiniz. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun dizini, gruptaki ilk satır veya sütun.
- Son satır/sütun dizini, gruptaki son satır veya sütun.
- Gizli mi, satırları/sütunları gruplandırmadan sonra gizlemek için bir Boolean parametre.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingRowsColumns.go" >}}

#### **Grup Ayarları**

Microsoft Excel, görüntüleme için grup ayarlarını yapılandırmanıza izin verir:

- Detayın altında özet satırlar.
- Ayrıntının sağında özet sütunlar.

## **Satır ve Sütunların Grubunu Çıkarma**

Herhangi bir gruplanmış satır veya sütunu çözmek için, [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [UngroupRows](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows/) ve [UngroupColumns](https://reference.aspose.com/cells/go-cpp/cells/ungroupcolumns/) yöntemlerini çağırın. Her iki yöntem de iki parametre alır:

- İlk satır veya sütun dizini, gruplandırılmış ilk satır/sütun.
- Son satır veya sütun dizini, gruplandırılmış son satır/sütun.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnGroupingRowsColumns.go" >}}
