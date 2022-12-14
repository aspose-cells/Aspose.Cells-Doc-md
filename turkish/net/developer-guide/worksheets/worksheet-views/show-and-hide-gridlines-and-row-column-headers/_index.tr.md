---
title: Kılavuz Çizgilerini ve Satır Sütun Başlıklarını Gösterme ve Gizleme
type: docs
weight: 30
url: /tr/net/show-and-hide-gridlines-and-row-column-headers/
---
{{% alert color="primary" %}}

Aspose.Cells, çalışma sayfasının varsayılan olarak görünen Kılavuz Çizgilerini gizlemeyi ve göstermeyi destekler. Ayrıca, çalışma sayfasının Satır Sütun Başlıklarının kontrol görünürlüğünü de sağlar.

{{% /alert %}}

## **Kılavuz Çizgilerini Göster ve Gizle**

Tüm Excel çalışma sayfalarında varsayılan olarak kılavuz çizgileri bulunur. Belirli hücrelere veri girmenin kolay olması için hücrelerin tanımlanmasına yardımcı olurlar. Kılavuz çizgileri, bir çalışma sayfasını, her hücrenin kolayca tanımlanabildiği bir hücreler koleksiyonu olarak görmemizi sağlar.

### **Kılavuz Çizgilerin Görünürlüğünü Kontrol Etme**

Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook), bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine izin veren koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, bir çalışma sayfasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Kılavuz çizgilerinin görünürlüğünü kontrol etmek için[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf[**Izgara Çizgileri Görünür mü**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) Emlak.[**Izgara Çizgileri Görünür mü**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) bir Boolean özelliğidir, yani yalnızca bir**doğru** veya**yanlış** değer.

#### **Kılavuz Çizgilerini Görünür Hale Getirme**

 ayarlayarak kılavuz çizgilerini görünür hale getirin.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf[**Izgara Çizgileri Görünür mü**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) mülkiyet**doğru**.

#### **Kılavuz Çizgilerini Gizleme**

 ayarlayarak kılavuz çizgilerini gizleyin.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf[**Izgara Çizgileri Görünür mü**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) mülkiyet**yanlış**.

 kullanımını gösteren tam bir örnek aşağıda verilmiştir.[**Izgara Çizgileri Görünür mü**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)özelliği, bir excel dosyasını (book1.xls) açarak, ilk çalışma sayfasındaki kılavuz çizgilerini gizleyerek ve değiştirilen dosyayı output.xls olarak kaydederek.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Satır Sütun Başlıklarını Göster ve Gizle**

Bir Excel dosyasındaki tüm çalışma sayfaları, satırlar ve sütunlar halinde düzenlenmiş hücrelerden oluşur. Tüm satırlar ve sütunlar, onları ve tek tek hücreleri tanımlamak için kullanılan benzersiz değerlere sahiptir. Örneğin, satırlar – 1, 2, 3, 4, vb. – numaralandırılır ve sütunlar alfabetik olarak sıralanır – A, B, C, D, vb. Başlıklarda satır ve sütun değerleri görüntülenir. Geliştiriciler, Aspose.Cells'i kullanarak bu satır ve sütun başlıklarının görünürlüğünü kontrol edebilir.

### **Çalışma Sayfalarının Görünürlüğünü Kontrol Etme**

Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook), bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine izin veren koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, bir çalışma sayfasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Satır ve sütun başlıklarının görünürlüğünü kontrol etmek için[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) Emlak.[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) bir Boolean özelliğidir, yani yalnızca bir**doğru** veya**yanlış**değer.

#### **Satır/Sütun Başlıklarını Görünür Hale Getirme**

 ayarlayarak satır ve sütun başlıklarını görünür hale getirin.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) mülkiyet**doğru**.

#### **Satır/Sütun Başlıklarını Gizleme**

 ayarlayarak satır ve sütun başlıklarını gizleyin.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) mülkiyet**yanlış**.

nasıl kullanılacağını gösteren eksiksiz bir örnek aşağıda verilmiştir.[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)özelliği, bir excel dosyasını (book1.xls) açarak, ilk çalışma sayfasındaki satır ve sütun başlıklarını gizleyerek ve değiştirilen dosyayı output.xls olarak kaydederek.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

 kullanmak da mümkündür.[**Satırları Göster**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) ve[**Sütunları Göster**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) yöntemleri[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) birden çok satırı ve sütunu görünür kılmak için sınıf.

{{% /alert %}}
