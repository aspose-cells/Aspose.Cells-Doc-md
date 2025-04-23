---
title: Aspose.Cells for Go via C++ Kurulum ve Go Komutu ile Kullanım.
type: docs
linktitle: Go Komutu ile Kurulum
weight: 40
url: /tr/go-cpp/how-to-install-aspose-cells-for-go-via-c++-using-the-go-command
---


## **Aspose.Cells for Go via C++ Nasıl Kurulur ve Go Komutu ile Kullanılır**

   Go 1.16'dan itibaren, `go install` komutunu doğrudan kullanarak Aspose.Cells for Go via C++ paketini kurabilirsiniz. Bu komut, komut satırı araçlarının küresel olarak kurulmasına olanak tanır ve mevcut proje bağımlılıklarını etkilemeden çalışır.

```go

go install github.com/aspose-cells/aspose-cells-go-cpp/v25@latest

```

   `go get` komutunu kullanarak Aspose.Cells for Go via C++ paketini kurduğunuzda, mevcut dizinde veya herhangi bir üst dizinde bir go.mod dosyasının bulunması gerekir. [projenizde Aspose.Cells for Go via C++ paketini yükleme ve kodunuzu çalıştırma](#Installation-in-your-project) ile ilgilidir.

```go

go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1

```

### Aspose.Cells for Go via C++ paketinin kurulumu ve projenizde kodunuzu çalıştırma {#Installation-in-your-project}

1. Projeniz için bir dizin oluşturun ve içinde main.go dosyası bulunmalı. main.go'nuza aşağıdaki kodu ekleyin.

```Go

package main

import (
 . "github.com/aspose-cells/aspose-cells-go-cpp/v25"
 "fmt"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String("YOUR_LICENSE_File_PATH")
 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_String_Bool("Hello World!", true)
 style, _ := cell.GetStyle()
 style.SetPattern(BackgroundType_Solid)
 color, _ := NewColor()
 color.Set_Color_R(uint8(255))
 color.Set_Color_G(uint8(128))
 style.SetForegroundColor(color)
 cell.SetStyle_Style(style)
 workbook.Save_String("HELLO.pdf")

}

```

1. Proje go.mod dosyasını başlatın

```bash

go mod init main

```

1. Projeniz için bağımlılıkları alın.

```bash

go mod tidy

```

Geliştirme ortamınıza Aspose.Cells for Go via C++ yüklü değilse, Go otomatik olarak paketi `$GOPATH` alt dizinine yükler.

1. Çalışmakta olan komut kabuğunuzda PATH'inizi Aspose.Cells for Go via C++ içindeki paylaşılan kütüphanelere işaret edecek şekilde ayarlayın. your_version yerine kullandığınız Aspose.Cells for Go via C++ sürümünü değiştirin.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1/lib/linux_x86_64/

```

Veya PowerShellinizde

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.1\lib\win_x86_64\"

```

Yukarıdaki dizinden DLL dosyalarını projenizin çalıştırılabilir dosyasıyla aynı yere kopyalayabilirsiniz.

1. Oluşturduğunuz uygulamayı çalıştırın.

```bash

go run main.go

```
