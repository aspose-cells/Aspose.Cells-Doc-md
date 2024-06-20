---
title: Levhaları Etkinleştirme ve Çalışma Kitabındaki Bir Hücreyi Etkinleştirme
type: docs
weight: 5
url: /tr/java/activating-sheets-and-activating-a-cell-in-worksheet/
---

{{% alert color="primary" %}}

Bazen, bir kullanıcı Microsoft Excel dosyasını Excel'de açtığında belirli bir çalışma sayfasının etkin ve görüntülenmesini isteyebilirsiniz. Benzer şekilde, belirli bir hücreyi etkinleştirmek ve kaydırmacıları etkin hücreyi göstermek isteyebilirsiniz. Aspose.Cells bunların tümünü aşağıda gösterildiği gibi yapabilir.

- **Etkin bir sayfa**, üzerinde çalıştığınız bir sayfadır: sekmedeki etkin sayfanın adı varsayılan olarak kalın harflerle yazılır.
- **Etkin bir hücre**, seçilen bir hücredir, veri girildiğinde verinin girilmeye başlandığı hücredir. Sadece bir hücre her seferinde etkin olabilir. Etkin hücre kalın bir kenarlıkla vurgulanır.

{{% /alert %}}

## **Levhaları Etkinleştirme ve Bir Hücreyi Etkinleştirme**

Aspose.Cells, bir sayfayı etkinleştirmek ve bir hücreyi etkinleştirmek için özel API çağrıları sağlar. Örneğin; [**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex) özelliği bir çalışma kitabında etkin sayfayı ayarlamak için kullanışlıdır. Benzer şekilde, [**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell) özelliği bir çalışma sayfasında etkin bir hücreyi ayarlamak ve almak için kullanılabilir.

Yatay veya dikey kaydırmacıların belirli bir veri satır ve sütun endeksi konumunda olduğundan emin olmak için [**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow) ve [**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn) özelliklerini kullanın.

Aşağıdaki örnek, bir çalışma sayfasını etkinleştirmeyi ve içinde etkin bir hücre oluşturmayı gösterir. Kodu çalıştırdığınızda aşağıdaki çıktı oluşturulur. Kaydırmacılar, ikinci satırı ve ikinci sütunu ilk görünür satır ve sütun olarak ayarlamak için kaydırılmıştır.

**B2 hücresini etkin hücre olarak ayarlama**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Excel'de bir etkin çalışma sayfası ayarlamak için Java kodu

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

**Değerlendirme** modunda, yani; geçerli bir lisans ayarlanmadan, etkin çalışma sayfası her zaman değerlendirme filigranını içeren sayfa olacaktır. Bu davranış sadece uygulamanın başında lisans ayarlanarak geçersiz kılınabilir.

{{% /alert %}}
