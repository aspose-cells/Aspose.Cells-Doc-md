---
title: Tablo Editörü  Sayfalarla Çalışma
type: docs
weight: 20
url: /tr/java/spreadsheet-editor-working-with-sheets/
---

**İçindekiler**

- [Sayfaları Ekle ve Kaldır?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
  - WorksheetView.onAddNewSheet
  - WorksheetView.onRemoveActiveSheet
- [Sayfaları Yeniden Adlandır](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
  - WorksheetView.setActiveSheet
- [Çalışma Sayfaları Arasında Geçiş Yapın](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
  - WorksheetView.setActiveSheet
### **Sayfaları Ekle ve Kaldır?**
Microsoft Excel tek bir dosyada birden çok sayfa izin verir. HTML5 Tablo Editörü kullanıcıya sayfa ekleyip kaldırma imkanı verir. Sayfalar sekmesinde bir sayfa için bir açılır liste bulunmaktadır. Seçilen sayfa düzenleyici tarafından açılan sayfadır.

Yeni bir sayfa eklemek için:

1. **Sayfaları** sekmesine geçin.
1. **+** (artı) düğmesine tıklayın.

Yeni bir sayfa eklenecek ve düzenleyici buna geçiş yapacaktır.

Şu an seçili sayfayı kaldırmak için:

1. **Sayfaları** sekmesine geçin.
1. **-** (eksi) düğmesine tıklayın.

Şu an seçili sayfa kaldırılacak ve düzenleyici son seçilen sayfaya geçecektir.

![todo:image_alt_text](4wgvmu8.png)

**Nasıl çalışır?**

Kullanıcı **+** (artı) ve **-** (eksi) düğmelerine tıkladığında, JSF backend bean **WorksheetView** olayları **WorksheetView.onAddNewSheet** ve **WorksheetView.onRemoveActiveSheet** metodları kullanarak işler.
#### **WorksheetView.onAddNewSheet**
{{< highlight java >}}

     public void onAddNewSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().add();

                getAsposeWorksheets().setActiveSheetIndex(i);

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("New Worksheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}

#### **WorksheetView.onRemoveActiveSheet**
{{< highlight java >}}

     public void onRemoveActiveSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().getActiveSheetIndex();

                getAsposeWorksheets().removeAt(i);

                if (getAsposeWorksheets().getCount() == 0) {

                    int j = getAsposeWorksheets().add();

                    getAsposeWorksheets().setActiveSheetIndex(j);

                }

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("Could not remove sheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}
### **Sayfaları Yeniden Adlandır**
Bir çalışma sayfasını yeniden adlandırmak için:

1. **Sayfaları** sekmesine geçin.
1. Metin kutusunda çalışma sayfasının adına tıklayın ve düzenlemek için düzenleyin.
1. Çalışma sayfasının adını değiştirin.
1. İşlemi bitirdiğinizde, ENTER tuşuna basın veya kutunun dışına herhangi bir yere tıklayın.

Çalışma sayfası yeniden adlandırılacak.

![todo:image_alt_text](4wgvmu8.png)

**Nasıl çalışır?**

Metin kutusu değeri değiştirildiğinde, etkinlik JSF arka uç fasulyesi **WorksheetView** kullanılarak **WorksheetView.setActiveSheet** yöntemi ile sunucuda işlenir.
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
### **Çalışma Sayfaları Arasında Geçiş Yapın**
Başka bir sayfaya geçmek için:

1. **Sayfaları** sekmesine geçin.
1. Açılır menüden bir sayfa seçin.

Düzenleyici seçilen sayfaya geçecek.

![todo:image_alt_text](4wgvmu8.png)

**Nasıl çalışır?**

Açılır menü seçicisi değeri değiştirildiğinde, etkinlik JSF arka uç fasulyesi **WorksheetView** kullanılarak **WorksheetView.setActiveSheet** yöntemi ile sunucuda işlenir.
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
