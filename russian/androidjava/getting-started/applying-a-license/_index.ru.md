---
title: Применение лицензии
type: docs
weight: 40
url: /ru/java/applying-a-license/
---

{{% alert color="primary" %}}

Как только вы будете удовлетворены своим оценочным периодом Aspose.Cells, [приобретите лицензию](https://purchase.aspose.com/buy) на веб-сайте Aspose. Ознакомьтесь с различными [типами лицензий](https://purchase.aspose.com/policies/license-types/), предлагаемыми. Если у вас возникнут вопросы, не стесняйтесь [связаться с отделом продаж Aspose](https://about.aspose.com/contact).

Каждая лицензия Aspose предоставляет бесплатную подписку на один год для бесплатного обновления до новых версий или исправлений, которые выходят за это время. Техническая поддержка бесплатна и неограниченная и предоставляется как лицензированным, так и оценочным пользователям.

Лицензия представляет собой простой текстовый XML-файл, содержащий сведения, такие как название продукта, количество лицензированных разработчиков, дату окончания подписки и т. д. Файл цифрово подписан, поэтому не изменяйте файл: даже добавление дополнительного перехода на новую строку в файле сделает его недействительным.

Перед выполнением любых операций с документами вам необходимо установить лицензию. Убедитесь, что вы сделали это перед созданием объекта Document. Вам необходимо установить лицензию только один раз для каждого приложения или процесса.

{{% /alert %}}

## **Загрузка файла лицензии**

В Aspose.Cells для Android via Java лицензию можно [встроить как ресурс](/cells/ru/java/applying-a-license/#applying-a-license-from-an-embedded-resource) или загрузить из потока:

1. Поместите файл лицензии в любое место на **/mnt/sdcard/**.
1. Создайте поток, указывающий на файл.
1. Передайте поток (содержащий файл лицензии) в метод SetLicense.

**Java**

{{< highlight java >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **Применение лицензии из встроенного ресурса**

Для доступа к лицензии как к ресурсу по имени из файла пакетной программы Android:

1. Добавьте файл лицензии в качестве ресурса в папку **res/raw** вашего приложения.
   Файл лицензии должен быть виден в папке **res/raw**.
1. Получите/загрузите лицензию из ресурса с помощью следующего фрагмента кода.

**Java**

{{< highlight java >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
