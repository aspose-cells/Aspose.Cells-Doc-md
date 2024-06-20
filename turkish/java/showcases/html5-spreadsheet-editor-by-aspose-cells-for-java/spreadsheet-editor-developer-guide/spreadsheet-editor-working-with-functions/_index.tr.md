---
title: Elektronik Tablo Düzenleyici  Fonksiyonlarla Çalışma
type: docs
weight: 60
url: /tr/java/spreadsheet-editor-working-with-functions/
---

**İçindekiler**

- [Formül Çubuğu](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [Bir Fonksiyon veya Formül Ekleme](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Formül Çubuğu**
Formül çubuğu, sayfa alanının üstünde bulunan bir metin kutusudur. Mevcut hücrenin formülünü gösterir ve kullanıcıya düzenleme yapma imkanı tanır.

**Nasıl çalışır?**

Bir hücre seçildiğinde formül çubuğu senkronize edilir ve formül gösterilir. Kullanıcı düzenleme izni verilir. Kullanıcı düzenleme yapar ve enter tuşuna basarsa, JavaScript fonksiyonu olan **saveFormulaBarContents** çalıştırılır.
#### **saveFormulaBarContents**
{{< highlight java >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Bir Fonksiyon veya Formül Ekleme**
Bir işlev veya formül eklemek için:

1. Bir hücreyi seçmek için tıklayın.
1. Üst kısımdaki **Fonksiyon Ekle** düğmesine tıklayın.
1. **Fonksiyon Ekle** iletişim kutusundaki talimatları izleyin.
