---
title: Gruplama, Gruplamanın Kaldırılması Satır ve Sütunlar
type: docs
weight: 30
url: /tr/cpp/grouping-ungrouping-rows-and-columns/
---

## **Giriş**
Bir Microsoft Excel dosyasında, veriler için bir biçim oluşturarak tek bir fare tıklamasıyla ayrıntı seviyelerini gösterip gizleyebilirsiniz.

Hızlıca sadece özet veya başlık sağlayan satırları veya sütunları veya ayrıntıları görmek için **Anahat Sembolleri** 1,2,3, + ve - düğmelerini tıklayın veya bir bireysel özet veya başlık altındaki ayrıntıları görmek için sembolleri kullanabilirsiniz.
## **Satır ve Sütunların Grup Yönetimi**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adında bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her sayfaya erişime izin veren bir [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonu içerir. Bir çalışsayfa [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışsayfadaki tüm hücreleri temsil eden bir [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu sağlar.

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu, çalışsayfadaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar, bunlardan bazıları aşağıda daha detaylı olarak tartışılmaktadır.
### **Satır ve Sütunların Gruplandırılması**
Satırları veya sütunları gruplamak, [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) ve [GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) yöntemlerini çağırarak mümkündür. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun dizini, gruptaki ilk satır veya sütun.
- Son satır/sütun dizini, gruptaki son satır veya sütun.
- Gizli mi, satırları/sütunları gruplandırmadan sonra gizlemek için bir Boolean parametre.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
#### **Grup Ayarları**
Microsoft Excel, görüntüleme için grup ayarlarını yapılandırmanıza izin verir:

- Detayın altında özet satırlar.
- Ayrıntının sağında özet sütunlar.
## **Satır ve Sütunların Grubunu Çıkarma**
Herhangi bir gruplanmış satır veya sütunu geri almak için, [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) ve [UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) yöntemlerini çağırın. Her iki yöntem de iki parametre alır:

- İlk satır veya sütun dizini, gruplandırılmış ilk satır/sütun.
- Son satır veya sütun dizini, gruplandırılmış son satır/sütun.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
