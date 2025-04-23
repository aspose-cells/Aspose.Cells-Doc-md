---
title: Başlarken
type: docs
weight: 10
url: /tr/go-cpp/getting-started/
description: Aspose Cells for Go yu C++ ile nasıl kurulur ve Merhaba Dünya uygulaması nasıl yapılır.
---

{{% alert color="primary" %}}

Bu sayfa, Aspose Cells for Go'yu C++ ile nasıl kuracağınızı ve Merhaba Dünya uygulaması nasıl oluşturacağınızı gösterecek.

{{% /alert %}}

## Aspose.Cells for Go via C++ entegrasyonu

Aspose.Cells for Go via C++ hoşgeldiniz! Bu çapraz platform çözüm Windows ve Linux'u destekliyor. Başlamak için, paket kullanan bir kod dosyasını çalıştırın.

### Ön Koşullar

- [Go (>=1.13)](https://golang.org/doc/install/)
- [Git](https://git-scm.com/downloads)

### Projenizde Aspose.Cells for Go via C++'yi Çalıştırma

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
 workbook.Save_String("HELLO.xlsx")

}

```

1. Proje go.mod dosyasını başlatın

```bash

go mod init main

```

1. Proje bağımlılıklarını alın.

```bash

go mod tidy

```

1. Çalışmakta olan komut kabuğunuzda PATH'inizi Aspose.Cells for Go via C++ içindeki paylaşılan kütüphanelere işaret edecek şekilde ayarlayın. your_version yerine kullandığınız Aspose.Cells for Go via C++ sürümünü değiştirin.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.0/lib/linux_x86_64/

```

Veya PowerShellinizde

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.0\lib\win_x86_64\"

```

Yukarıdaki dizinden DLL dosyalarını projenizin çalıştırılabilir dosyasıyla aynı yere kopyalayabilirsiniz.

1. Oluşturduğunuz uygulamayı çalıştırın.

```bash

go run main.go

```
