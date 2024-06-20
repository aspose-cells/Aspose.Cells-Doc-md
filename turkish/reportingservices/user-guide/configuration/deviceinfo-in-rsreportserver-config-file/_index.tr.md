---
title: rsreportserver.config dosyasındaki DeviceInfo
type: docs
weight: 70
url: /tr/reportingservices/deviceinfo-in-rsreportserver-config-file/
---

**rsreportserver.config** içindeki DeviceInfo bölümü, Aspose.Cells'in davranışını etkileyen aşağıdaki parametreleri alır:

- **FileExtension**: değer null ise, dışa aktarılan rapor dosya uzantısı varsayılan değere ayarlanır. Değer null değilse, raporun uzantısı değere ayarlanır.
- **SimplePageHeaders**: değer **true** ise, rapor başlık öğesi bir Microsoft Excel sayfa başlığı olarak işlenir. Varsayılan değer **false**'dur.
- **SimplePageFooters**: **true** ise, rapor altbilgi öğesi bir Microsoft Excel sayfa altbilgi olarak işlenir. Varsayılan değer **true**'dir.
- **PutoutHeader**: **true** ise (varsayılan), rapor başlık öğesi dışa aktarılır. **false** ise, rapor başlık öğesi dışa aktarılmaz. Yalnızca Excel 2007 XLSX (yalnızca veri) uzantısını destekler.
- **PutoutFooter**: **true** ise (varsayılan), rapor altbilgi öğesi dışa aktarılır. **false** ise, dışa aktarılmaz. Yalnızca Excel 2007 XLSX (yalnızca veri) uzantısını destekler.
- **FillTableGroupHeaderForSimpleOutPut**: varsayılan olarak **false**'dur. Değer, yalnızca Excel 2007 XLSX (yalnızca veri) uzantısını destekler.
- **NoOutPutTotalForSimpleOutPut**: varsayılan olarak **false**'dur. Değer, yalnızca Excel 2007 XLSX (yalnızca veri) uzantısını destekler.
- **SimpleOutput İçin Çıktı Grubu Yok**: Varsayılan olarak **false**. Değer yalnızca Excel 2007 XLSX (yalnız veri) uzantısını destekler.
- Varsayılan olarak **SimpleOutput İçin Doğrusal Grup Sayfası Yok**: **true**. Değer yalnızca Excel 2007 XLSX (yalnız veri) uzantısını destekler.
- Varsayılan olarak **SimpleOutput İçin Doğrusal Sayfa Yok**: **true**. Değer yalnızca Excel 2007 XLSX (yalnız veri) uzantısını destekler.
- **FieldDelimiter**: alan ayırıcıları ayarlar. Değer CSV ve TXT uzantılarını destekler.
