---
title: Satırları ve Sütunları Gruplandırma, Grubu Çözme
type: docs
weight: 30
url: /tr/cpp/grouping-ungrouping-rows-and-columns/
---
## **giriiş**
Bir Microsoft Excel dosyasında, tek bir fare tıklamasıyla ayrıntı düzeylerini göstermenize ve gizlemenize olanak tanıyan veriler için bir ana hat oluşturabilirsiniz.

 Tıkla**Anahat Sembolleri**, 1,2,3, + ve - yalnızca bir çalışma sayfasındaki bölümler için özetler veya başlıklar sağlayan satırları veya sütunları hızlı bir şekilde görüntülemek için veya ayrı bir özet veya başlık altındaki ayrıntıları görmek için sembolleri kullanabilirsiniz.
## **Satırlar ve Sütunların Grup Yönetimi**
 Aspose.Cells bir sınıf sağlar,[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[IÇalışma Sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf bir sağlar[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 bu[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar; bunlardan birkaçı aşağıda daha ayrıntılı olarak ele alınmıştır.
### **Satırları ve Sütunları Gruplama**
 çağırarak satırları veya sütunları gruplandırmak mümkündür.[GrupSatırları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a88e0180ed1a4a423e0bd3ac599ef9332) ve[Grup Sütunları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aaa14179e2a84ba5c2857f8434570d3d8) yöntemleri[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Toplamak. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun dizini, gruptaki ilk satır veya sütun.
- Gruptaki son satır/sütun dizini, son satır veya sütun.
- Gizlidir, gruplamadan sonra satırların/sütunların gizlenip gizlenmeyeceğini belirten bir Boolean parametresidir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns.cpp" >}}
#### **Grup Ayarları**
Microsoft Excel, aşağıdakileri görüntülemek için grup ayarlarını yapılandırmanıza izin verir:

- Ayrıntıların altındaki özet satırları.
- Ayrıntıların sağındaki özet sütunları.
## **Satırları ve Sütunları Çözme**
 Gruplanmış herhangi bir satır veya sütunun grubunu çözmek için,[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) koleksiyonun[Satırları Çöz](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#adc1f6418506854ab41707bfef453ddb1) ve[Sütunların Grubunu Çöz](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aa3bf9a9510d4e85f68db9ebdcadc8406)yöntemler. Her iki yöntem de iki parametre alır:

- İlk satır veya sütun dizini, grubu çözülecek ilk satır/sütun.
- Son satır veya sütun dizini, grubu çözülecek son satır/sütun.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns.cpp" >}}
