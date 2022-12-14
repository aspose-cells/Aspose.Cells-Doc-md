---
title: Aspose.Cells .NET для PHP
type: docs
weight: 40
url: /ru/net/aspose-cells-net-for-php/
---
## **Начиная**

### **Введение**

### **Системные требования и поддерживаемые платформы**

#### **Системные Требования**

**Ниже приведены системные требования для использования Aspose.Cells .NET для PHP:**

- IIS с установленным PHP и PHP Manager.
- Aspose.Total API.
- Aspose.Cells DLL-файл Interop и файл tlb.

#### **Поддерживаемые платформы**

**Ниже приведены поддерживаемые платформы:**

- PHP 5.3 или выше
- Windows ОС

### **Скачать и настроить**

#### **Скачать необходимые библиотеки**

Загрузите необходимые библиотеки, указанные ниже. Они необходимы для выполнения Aspose.Cells Java для примеров PHP.

- [Загрузите файлы Aspose.Cells for .NET (DLL или MSI) из раздела загрузки](https://downloads.aspose.com/cells/net)
- [Скачать Aspose.Cells for .NET интероп dll](https://downloads.aspose.com/cells/net)

Если вы загрузите версию MSI, вы найдете Aspose.Cells.dll в установленном месте, которое по умолчанию находится в папке C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0.
Однако, если вы загрузили версию DLL, вы можете извлечь ее, а затем скопировать Aspose.Cells.dll из папки .NET 2.0 в папку c:\temp для простоты использования.
Аналогичным образом извлеките zip-файл взаимодействия и скопируйте Aspose.Inteop.dll в c:\temp.

#### **Загрузите примеры с сайтов социального кодирования**

Следующие выпуски работающих примеров доступны для загрузки на указанных ниже сайтах социального кодирования:

-----

##### **Гитхаб**

- **Aspose.Cells .NET для примеров PHP**

  - [Aspose.Cells .NET для PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Как настроить исходный код на платформе Windows**

Пожалуйста, следуйте этим простым шагам, чтобы открыть и расширить исходный код при использовании:

##### **1. Зарегистрируйте файлы dll и interop.dll, например Aspose.Cells.dll и Aspose.Cells.Interop.dll.**

{{< highlight "java" >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Включите расширения COM и DOTNET в PHP.**

В IIS откройте диспетчер PHP, а затем нажмите «Включить, чтобы отключить и расширение». Найти php_ком_dotnet.dll и убедитесь, что он включен.

##### **3. Настройте Aspose.Cells .NET для примеров PHP**

###### **Способ 1**

 Клонировать примеры PHP из[гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
и выполните следующую команду

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

###### **Способ 2**

В файле composer.json вашего PHP-проекта добавьте следующие строки

{{< highlight "java" >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

и запустите команду установки

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

 Читать о визите композитора<https://getcomposer.org/>

### **Поддержка, расширение и участие**

#### **Поддерживать**

С самых первых дней Aspose мы знали, что просто предоставлять нашим клиентам хорошие продукты будет недостаточно. Нам также нужно было обеспечить хорошее обслуживание. Мы сами являемся разработчиками и понимаем, как это неприятно, когда техническая проблема или особенность программного обеспечения мешают вам делать то, что вам нужно. Мы здесь, чтобы решать проблемы, а не создавать их.

Вот почему мы предлагаем бесплатную поддержку. Любой, кто использует наш продукт, независимо от того, купили ли они его или используют для ознакомления, заслуживает нашего полного внимания и уважения.

Вы можете зарегистрировать любые проблемы или предложения, связанные с Aspose.Cells .NET для PHP, используя любую из следующих платформ:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Расширяйте и вносите свой вклад**

Aspose.Cells .NET для PHP имеет открытый исходный код, и его исходный код доступен на основных веб-сайтах социального кодирования, перечисленных ниже. Разработчикам рекомендуется загружать исходный код и вносить свой вклад, предлагая или добавляя новые функции или улучшая существующие, чтобы другие также могли извлечь из этого пользу.

#### **Исходный код**

Вы можете получить последний исходный код из одного из следующих мест

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Образцы кода**

В этот раздел входят следующие темы

- [Руководство для программистов PHP](/cells/ru/net/php-programmers-guide/)
  - [Работа с файлами в PHP.](/cells/ru/net/working-with-files-in-php/)
    - [Особенности работы с файлами в PHP](/cells/ru/net/file-handling-features-in-php/)
      - [Открытие файлов в PHP](/cells/ru/net/opening-files-in-php/)
      - [Сохранение файлов в PHP](/cells/ru/net/saving-files-in-php/)
    - [Служебные функции в PHP](/cells/ru/net/utility-features-in-php/)
      - [Шифрование файлов в PHP](/cells/ru/net/encrypting-files-in-php/)
      - [Преобразование Excel в PDF в PHP](/cells/ru/net/excel-to-pdf-conversion-in-php/)
      - [Управление свойствами документа в PHP](/cells/ru/net/managing-document-properties-in-php/)
      - [Преобразование рабочего листа в изображение в PHP](/cells/ru/net/worksheet-to-image-conversion-in-php/)
  - [Работа с формулами в PHP.](/cells/ru/net/working-with-formulas-in-php/)
    - [Вычисление формул в PHP](/cells/ru/net/calculating-formulas-in-php/)
  - [Работа с листами в PHP](/cells/ru/net/working-with-worksheets-in-php/)
    - [Функции управления в PHP](/cells/ru/net/management-features-in-php/)
      - [Управление рабочими листами в PHP](/cells/ru/net/managing-worksheets-in-php/)
        - [Добавить рабочие листы в существующий файл Excel в PHP](/cells/ru/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Добавить рабочие листы в новый файл Excel в PHP](/cells/ru/net/add-worksheets-to-new-excel-file-in-php/)
        - [Удаление рабочих листов с помощью индекса листа в PHP](/cells/ru/net/removing-worksheets-using-sheet-index-in-php/)
        - [Удаление рабочих листов с использованием имени листа в PHP](/cells/ru/net/removing-worksheets-using-sheet-name-in-php/)
