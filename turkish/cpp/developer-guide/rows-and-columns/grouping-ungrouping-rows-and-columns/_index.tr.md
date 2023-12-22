---
title: Satır ve Sütunların Gruplandırılması, Grubunun Çözülmesi
type: docs
weight: 30
url: /tr/cpp/grouping-ungrouping-rows-and-columns/
---
##  **giriiş**
Microsoft Excel dosyasında, tek bir fare tıklamasıyla ayrıntı düzeylerini göstermenize ve gizlemenize olanak tanıyan veriler için bir taslak oluşturabilirsiniz.

Yalnızca bir çalışma sayfasındaki bölümlerin özetlerini veya başlıklarını sağlayan satırları veya sütunları hızlı bir şekilde görüntülemek için *Anahat Sembolleri**, 1,2,3, + ve -'yi tıklayın veya bireysel bir özetin altındaki ayrıntıları görmek için sembolleri kullanabilirsiniz veya başlık.
##  **Satır ve Sütunların Grup Yönetimi**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf sağlar[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)toplama, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar; bunlardan birkaçı aşağıda daha ayrıntılı olarak tartışılmaktadır.
###  **Satırları ve Sütunları Gruplandırma**
 Çağrılarak satırları veya sütunları gruplamak mümkündür.[GrupSatırları](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) Ve[GrupSütunları](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) yöntemleri[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Toplamak. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun dizini, gruptaki ilk satır veya sütun.
- Son satır/sütun dizini, gruptaki son satır veya sütun.
- Gizlidir, gruplandırma sonrasında satırların/sütunların gizlenip gizlenmeyeceğini belirten bir Boolean parametresidir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
####  **Grup Ayarları**
Microsoft Excel, aşağıdakileri görüntülemek için grup ayarlarını yapılandırmanıza olanak tanır:

- Ayrıntıların altındaki özet satırları.
- Detayın sağındaki özet sütunları.
##  **Satırların ve Sütunların Grubunu Çözme**
 Gruplandırılmış herhangi bir satır veya sütunun grubunu çözmek için[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Koleksiyonun[Satırların Grubunu Çöz](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) Ve[Sütunların Grubunu Çöz](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)yöntemler. Her iki yöntem de iki parametre alır:

- İlk satır veya sütun dizini, grubu çözülecek ilk satır/sütun.
- Son satır veya sütun dizini, grubu çözülecek son satır/sütun.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
