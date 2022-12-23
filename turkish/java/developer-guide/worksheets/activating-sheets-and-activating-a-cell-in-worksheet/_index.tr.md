---
title: Sayfaları Etkinleştirme ve Çalışma Sayfasında Cell'i Etkinleştirme
type: docs
weight: 5
url: /tr/java/activating-sheets-and-activating-a-cell-in-worksheet/
---
{{% alert color="primary" %}}

Bazen, bir kullanıcı bir Microsoft Excel dosyasını Excel'de açtığında belirli bir çalışma sayfasının etkin olması ve görüntülenmesi gerekir. Benzer şekilde, belirli bir hücreyi etkinleştirmek ve kaydırma çubuklarını etkin hücreyi gösterecek şekilde ayarlamak isteyebilirsiniz. Aspose.Cells, aşağıda gösterildiği gibi tüm bu görevleri yapabilir.

-  Bir**etkin sayfa** üzerinde çalıştığınız bir sayfadır: sekmedeki etkin sayfanın adı varsayılan olarak kalındır.
-  Bir**aktif hücre** seçili bir hücredir, yazmaya başladığınızda verilerin girildiği hücredir. Aynı anda yalnızca bir hücre etkindir. Etkin hücre kalın bir kenarlıkla vurgulanır.

{{% /alert %}}

## **Sayfaları Etkinleştirme ve Cell'i Etkinleştirme**

Aspose.Cells, bir sayfa ve hücreyi etkinleştirmek için özel API çağrıları sağlar. Örneğin,[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex)özelliği, bir çalışma kitabındaki etkin sayfayı ayarlamak için kullanışlıdır. Benzer şekilde,[**Çalışma Sayfası.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell)özelliği, çalışma sayfasında etkin bir hücre ayarlamak ve almak için kullanılabilir.

Yatay veya dikey kaydırma çubuklarının, belirli verileri göstermek istediğiniz satır ve sütun dizini konumunda olduğundan emin olmak için,[**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow)ve[**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn)özellikler.

Aşağıdaki örnek, bir çalışma sayfasının nasıl etkinleştirileceğini ve içinde etkin bir hücrenin nasıl oluşturulacağını gösterir. Kod yürütülürken aşağıdaki çıktı oluşturulur. Kaydırma çubukları, 2. satırı ve 2. sütunu ilk görünür satır ve sütunları yapmak için kaydırılır.

**B2 hücresini aktif hücre olarak ayarlama**

![yapılacaklar:resim_alternatif_metin](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Excel'de etkin bir çalışma sayfası ayarlamak için Java kodu

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

 İçinde**değerlendirme**mod, yani; geçerli bir lisans ayarlamadan, etkin çalışma sayfası her zaman değerlendirme filigranını içeren çalışma sayfası olacaktır. Bu davranış, yalnızca uygulamanın başlangıcında lisans ayarlanarak geçersiz kılınabilir.

{{% /alert %}}
