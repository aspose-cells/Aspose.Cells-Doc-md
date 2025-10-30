---
title: Çalışma Kitabının Formül Hesaplama Modunu Ayarlama ve Golang ile C++ Kullanımı
linktitle: Çalışbook un Formül Hesaplama Modunu Ayarlama
description: Bu makale, C++ kullanarak Aspose.Cells kütüphanesi ile Microsoft Excel de bir çalışma kitabının formül hesaplama modunu nasıl ayarlayacağınızı tanıtmaktadır. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemi kullanarak formül hesaplama modunu ayarlayabilir ve sonucu alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, çalışma kitabı, formül hesaplama modu, ayarlar, C++
type: docs
weight: 110
url: /tr/go-cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel, formül hesaplama modunu, yani formüllerin nasıl hesaplandığını ayarlamanıza izin verir. Üç olası değer bulunmaktadır:

- Otomatik - bir şey değiştirildiğinde ve her bir çalışma kitabı açıldığında yeniden hesapla.
- Otomatik, veri tabloları hariç - bir şey değiştirildiğinde yeniden hesapla, ancak veri tablolarını dışarıda bırak.
- Manuel - kullanıcı açıkça istediğinde (F9 veya CTRL+ALT+F9'a basarak) veya çalışma kitabı kaydedildiğinde sadece yeniden hesapla.

{{% /alert %}}

Microsoft Excel'de formül hesaplama modunu ayarlamak için:

1. **Formüller**'i seçin, ardından **Hesaplama Seçenekleri**'ni seçin.
1. Seçeneklerden birini seçin.

Aspose.Cells ayrıca, [**FormulaSettings.GetCalculationMode()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getcalculationmode/) mod özelliğini kullanarak **Formül Hesaplama Modunu** ayarlamanıza izin verir. Bu özelliği, aşağıdaki değerlerden birine sahip olan [**CalcModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/calcmodetype/) numaralandırmasına atayabilirsiniz:

- CalcModeType::Automatic
- CalcModeType::AutomaticExceptTable
- CalcModeType::Manual

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingFormulaCalculationModeOfWorkbook.go" >}}
