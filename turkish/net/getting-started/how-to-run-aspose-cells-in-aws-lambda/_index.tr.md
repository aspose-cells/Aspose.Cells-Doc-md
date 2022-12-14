---
title: AWS Lambda'da Aspose.Cells Nasıl Çalıştırılır
type: docs
description: Geliştirme yığınınızda hangi teknolojinin bulunduğundan bağımsız olarak Docker kullanarak Aspose.Cells işlevselliğini uygulamanıza entegre edin. Docker kapsayıcısında Aspose .Cells'i nasıl kullanacağınızı öğrenin
weight: 141
url: /tr/net/how-to-run-aspose-cells-in-aws-lambda/
---
## AWS ortamını hazırlayın

1.  Bir AWS hesabı kaydedin:
[AWS hesabını kaydedin](https://aws.amazon.com/)
1. AWS hesabınızda oturum açın, hesabınızın altına bir IAM kullanıcısı ekleyin. AWS resmi belgesine başvurabilirsiniz:
[IAM kullanıcısı ekle](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. “AmazonS3FullAccess” izni ekleyin, lütfen aynı şekilde kullanın, EC2 ve Elastic Beanstalk'ı ekleyin, her biri için tam erişim.
1. Son adımda IAM kullanıcı adı, Key, Key ID ve “credentials.csv” dosyasını aldığınızdan emin olun, bunları iyi kaydetmeniz gerekiyor.
 Şimdi IAM kullanıcınızın S3, EC2, Elastic Beanstalk ve tam erişime sahip olduğundan emin olun. görmek:
   
**![AWS Erişimi](AwsAccess.png)**

## AWS Toolkit for Visual Studio'yu yükleyin

1. Visual Studio 2019 veya üzeri sürümü kurun.
1.  AWS Toolkit for Visual Studio'yu indirip yükleyin:
[AWS Araç Seti](https://aws.amazon.com/visualstudio/)

## AWS Lambda'da çalışan bir proje oluşturun

1. Visual Studio'da bir ASP.NET Çekirdek Web Uygulaması oluşturun, test kodu yazın, nuget'den Aspose.Cells'i alın.

1. Test projesinin yerel makinenizde iyi çalıştığından emin olun, ardından onu AWS Elastic Beanstalk'a dağıtın:
 Proje adına sağ tıklayın, "AWS Elastic Beanstalk'ta Yayınla"yı seçin. (Bu seçenek yalnızca AWS Toolkit for Visual Studio'yu yükledikten sonra mevcut olacaktır).
1.  AWS hesabınız ve IAM kullanıcınızla yeni bir kullanıcı eklemeniz gerekecek, önceki adımda aldığınız "credentials.csv" dosyasını içe aktarabilirsiniz.
1. Yayın başarılı, şöyle bir link adresi alacaksınız: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
 Bağlantının etkinleşmesi için 10 dakika bekleyin, ardından ziyaret edebilirsiniz!
