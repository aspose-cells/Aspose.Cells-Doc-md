---
title: Начало работы
type: docs
weight: 10
url: /ru/go-cpp/getting-started/
description: Как установить Aspose Cells для Go через C++ и создать приложение Hello World.
---

{{% alert color="primary" %}}

Эта страница покажет вам, как установить Aspose Cells for Go через C++ и создать приложение Hello World.

{{% /alert %}}

## Интеграция Aspose.Cells for Go via C++

Добро пожаловать в Aspose.Cells for Go via C++! Это кроссплатформенное решение поддерживает как Windows, так и Linux. Чтобы начать, выполните файл кода, использующий пакет.

### Предварительные требования

- [Go (>=1.13)](https://golang.org/doc/install/)
- [Git](https://git-scm.com/downloads)

### Запуск Aspose.Cells for Go via C++ в вашем проекте

1. Создайте каталог для вашего проекта и файл main.go внутри. Добавьте следующий код в ваш main.go.

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

1. Инициализируйте проект go.mod

```bash

go mod init main

```

1. Получите зависимости для проекта.

```bash

go mod tidy

```

1. Установите переменную PATH, указывающую на общие библиотеки в Aspose.Cells for Go via C++ в вашей текущей командной оболочке. Замените your_version на версию Aspose.Cells for Go via C++, которую вы используете.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.0/lib/linux_x86_64/

```

Или в PowerShell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.0\lib\win_x86_64\"

```

Вы также можете скопировать файлы DLL из вышеназванного пути в то же место, где находится ваш исполняемый файл проекта.

1. Запустите созданное вами приложение.

```bash

go run main.go

```
