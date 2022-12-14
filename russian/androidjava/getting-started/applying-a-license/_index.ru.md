---
title: Применение лицензии
type: docs
weight: 40
url: /ru/java/applying-a-license/
---
{{% alert color="primary" %}}

 Как только вы будете довольны своей оценкой Aspose.Cells,[купить лицензию](https://purchase.aspose.com/buy) на сайте Aspose. Познакомьтесь с различными[типы лицензий](https://purchase.aspose.com/policies/license-types/) предложил. Если у вас есть какие-либо вопросы, не стесняйтесь[свяжитесь с отделом продаж Aspose](https://about.aspose.com/contact).

Каждая лицензия Aspose включает годовую подписку на бесплатные обновления до любых новых версий или исправлений, которые выйдут в течение этого времени. Техническая поддержка бесплатна и неограниченна и предоставляется как лицензированным, так и ознакомительным пользователям.

Лицензия представляет собой обычный текстовый XML-файл, который содержит такие сведения, как название продукта, количество лицензированных разработчиков, дату истечения срока действия подписки и т. д. Файл имеет цифровую подпись, поэтому не изменяйте файл: даже добавление в файл дополнительного разрыва строки сделает его недействительным.

Перед выполнением любых операций с документами необходимо установить лицензию. Обязательно сделайте это перед созданием объекта Document. Вы должны установить лицензию только один раз для каждого приложения или процесса.

{{% /alert %}}

## **Загрузка файла лицензии**

 В Aspose.Cells для Android через Java лицензию можно[встроенный как ресурс](/cells/ru/java/applying-a-license/#applying-a-license-from-an-embedded-resource)или загружается из потока:

1.  Поместите файл лицензии в любое место на**/мнт/sdcard/**.
1. Создайте поток, который ссылается на файл.
1. Передайте поток (содержащий файл лицензии) в метод SetLicense.

**Java**

{{< highlight "java" >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **Применение лицензии из встроенного ресурса**

Чтобы получить доступ к лицензии как к ресурсу по имени из файла пакета Android:

1.  Добавьте файл лицензии в качестве ресурса в папку вашего приложения.**разрешение/сырье** папка.
 Файл лицензии должен быть виден в**разрешение/сырье** папка.
1. Получите доступ/загрузите лицензию из ресурса с помощью следующего примера кода.

**Java**

{{< highlight "java" >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
