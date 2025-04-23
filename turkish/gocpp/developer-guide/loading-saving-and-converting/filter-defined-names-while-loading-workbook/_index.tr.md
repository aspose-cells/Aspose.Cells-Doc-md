---
title: Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele
type: docs
weight: 50
url: /tr/go-cpp/filter-defined-names-while-loading-workbook/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabı içinde tanımlanmış adları filtrelemenize veya kaldırmanıza imkan tanır. Çalışma kitabını yüklerken tanımlı adları yüklemek için [**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) kullanın. Tanımlı adları kaldırırsanız, çalışma içindeki formüller bozulabilir.

## **Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele**

Aşağıdaki örnek kod, formülü **C1** hücresinde bulunan [örnek Excel dosyasını](61767860.xlsx) yükler; burada tanımlı adlar, *=SUM(MyName1, MyName2)* içerir. Dosya yüklenirken ~[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/)'ı kullanarak tanımlı adları kaldırdığımızda, [çıktı Excel dosyasındaki](61767861.xlsx) formül bozulur ve yerine *#NAME?* görüntülenir. Kodun etkisini gösteren aşağıdaki ekran görüntüsüne bakın.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterDefinedNamesWhileLoadingWorkbook.go" >}}
