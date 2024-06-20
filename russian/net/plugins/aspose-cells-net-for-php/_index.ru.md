---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /ru/net/aspose-cells-net-for-php/
---

## **Начало работы**

### **Введение**

### **Требования к системе и поддерживаемые платформы**

#### **Системные требования**

**Ниже приведены системные требования для использования Aspose.Cells .NET для PHP:**

- IIS с установленными PHP и PHP Manager.
- Aspose.Total APIs.
- Aspose.Cells интероп dll и tlb файл.

#### **Поддерживаемые платформы**

**Ниже приведены поддерживаемые платформы:**

- PHP 5.3 или выше
- ОС Windows

### **Загрузка и настройка**

#### **Загрузить необходимые библиотеки**

Загрузите необходимые библиотеки, указанные ниже. Они необходимы для выполнения примеров Aspose.Cells Java для PHP.

- [Загрузите файлы Aspose.Cells for .NET (DLL или MSI) из раздела загрузок](https://downloads.aspose.com/cells/net)
- [Загрузите Aspose.Cells for .NET интероп dll](https://downloads.aspose.com/cells/net)

Если вы загрузили версию MSI, вы найдете Aspose.Cells.dll в установленном местоположении, которое по умолчанию находится в папке C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0.
Однако, если вы загрузили версию DLL, вы можете извлечь ее и затем скопировать Aspose.Cells.dll из папки .NET 2.0 в вашу папку c:\temp для удобства использования.
Точно так же извлеките zip-файл интеропа и скопируйте Aspose.Inteop.dll в c:\temp

#### **Загрузить примеры из сайтов социального кодирования**

Следующие версии выполняемых примеров доступны для загрузки на указанных ниже сайтах социального кодирования:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Examples**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Как настроить исходный код на платформе Windows**

Пожалуйста, следуйте этим простым шагам для открытия и расширения исходного кода при использовании:

##### **1. Зарегистрируйте файлы dll и interop.dll, например Aspose.Cells.dll и Aspose.Cells.Interop.dll.**

{{< highlight java >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Включите расширения COM и DOTNET в PHP.**

В IIS откройте PHP Manager и затем нажмите «Включить или отключить расширение». Найдите файл php_com_dotnet.dll и убедитесь, что он включен.

##### **3. Настройте примеры Aspose.Cells .NET для PHP**

###### **Метод 1**

Клонируйте примеры PHP из [github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
и выполните следующую команду

{{< highlight java >}}

 composer install

{{< /highlight >}}

###### **Метод 2**

В файл composer.json вашего PHP-проекта добавьте следующие строки

{{< highlight java >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

и выполните команду установки

{{< highlight java >}}

 composer install

{{< /highlight >}}

To read about composer visit <https://getcomposer.org/>

### **Поддержка Расширение и Участие**

#### **Поддержка**

С самых первых дней Aspose мы поняли, что просто предоставить нашим клиентам хорошие продукты недостаточно. Нам также необходимо предоставлять хорошее обслуживание. Мы сами являемся разработчиками и понимаем, насколько раздражающе, когда техническая проблема или особенность программного обеспечения мешает вам делать то, что вам необходимо. Мы здесь, чтобы решать проблемы, а не создавать их.

Поэтому мы предлагаем бесплатную поддержку. Каждый, кто использует наш продукт, независимо от того, купил он их или использует оценку, заслуживает нашего внимания и уважения.

Вы можете сообщить о любых проблемах или предложениях, касающихся Aspose.Cells .NET для PHP, используя любую из следующих платформ:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Расширение и вклад**

Aspose.Cells .NET для PHP - это открытый исходный код, и его исходный код доступен на основных веб-сайтах для разработчиков, перечисленных ниже. Разработчиков призывают загружать исходный код и вносить предложения или добавлять новые функции либо улучшать существующие, чтобы другие могли также извлечь пользу из этого.

#### **Исходный код**

Вы можете получить последний исходный код в одном из следующих мест

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Примеры кода**

В этом разделе содержатся следующие темы

- [Руководство программиста PHP](/cells/ru/net/php-programmers-guide/)
  - [Работа с файлами в PHP](/cells/ru/net/working-with-files-in-php/)
    - [Работа с файлами в PHP](/cells/ru/net/file-handling-features-in-php/)
      - [Открытие файлов в PHP](/cells/ru/net/opening-files-in-php/)
      - [Сохранение файлов в PHP](/cells/ru/net/saving-files-in-php/)
    - [Вспомогательные функции в PHP](/cells/ru/net/utility-features-in-php/)
      - [Шифрование файлов в PHP](/cells/ru/net/encrypting-files-in-php/)
      - [Преобразование Excel в PDF в PHP](/cells/ru/net/excel-to-pdf-conversion-in-php/)
      - [Управление свойствами документа в PHP](/cells/ru/net/managing-document-properties-in-php/)
      - [Преобразование таблицы в изображение в PHP](/cells/ru/net/worksheet-to-image-conversion-in-php/)
  - [Работа с формулами в PHP](/cells/ru/net/working-with-formulas-in-php/)
    - [Вычисление формул в PHP](/cells/ru/net/calculating-formulas-in-php/)
  - [Работа с рабочими листами в PHP](/cells/ru/net/working-with-worksheets-in-php/)
    - [Функции управления в PHP](/cells/ru/net/management-features-in-php/)
      - [Управление рабочими листами в PHP](/cells/ru/net/managing-worksheets-in-php/)
        - [Добавление рабочих листов в существующий файл Excel в PHP](/cells/ru/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Добавление рабочих листов в новый файл Excel в PHP](/cells/ru/net/add-worksheets-to-new-excel-file-in-php/)
        - [Удаление рабочих листов с использованием индекса листа в PHP](/cells/ru/net/removing-worksheets-using-sheet-index-in-php/)
        - [Удаление рабочих листов с использованием имени листа в PHP](/cells/ru/net/removing-worksheets-using-sheet-name-in-php/)
