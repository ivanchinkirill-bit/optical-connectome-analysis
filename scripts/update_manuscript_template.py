#!/usr/bin/env python3
"""
ШАБЛОН ДЛЯ ОБНОВЛЕНИЯ РУКОПИСИ
==============================

Обновляет рукопись с DOI и GitHub URL

Автор: Optical Connectome Research Team
"""

def update_manuscript_with_doi(doi_url, github_url):
    """Обновить рукопись с DOI и GitHub URL"""
    
    # Читаем текущую рукопись
    with open('arxiv_preprint_final.md', 'r') as f:
        content = f.read()
    
    # Заменяем DOI
    content = content.replace(
        '**DOI**: [To be assigned upon publication]',
        f'**DOI**: {doi_url}'
    )
    
    # Заменяем GitHub URL
    content = content.replace(
        'https://github.com/optical-connectome/optical-connectome-analysis',
        github_url
    )
    
    # Сохраняем обновленную рукопись
    with open('arxiv_preprint_final_updated.md', 'w') as f:
        f.write(content)
    
    print(f"✅ Рукопись обновлена:")
    print(f"   DOI: {doi_url}")
    print(f"   GitHub: {github_url}")
    print(f"   Файл: arxiv_preprint_final_updated.md")

def create_arxiv_upload_instructions():
    """Создать инструкции для загрузки на arXiv"""
    
    instructions = """# ИНСТРУКЦИИ ПО ЗАГРУЗКЕ НА ARXIV

## 🎯 ЦЕЛЬ
Загрузить препринт на arXiv для защиты приоритета

## 📋 ПЛАН ДЕЙСТВИЙ

### 1. ПОДГОТОВКА ФАЙЛОВ

#### Основные файлы:
- `arxiv_preprint_final_updated.md` - рукопись
- `Figure1_Distributions.png` - графики
- `Figure2_Correlations.png`
- `Figure3_3D_Tracts.png`
- `Figure4_Network.png`
- `Figure5_Dataset_Comparison.png`
- `ROC_Analysis.png`

#### Создать архив:
```bash
tar -czf arxiv_submission.tar.gz arxiv_preprint_final_updated.md *.png
```

### 2. ЗАГРУЗКА НА ARXIV

#### Перейти на https://arxiv.org
1. Нажать "Submit"
2. Выбрать категорию: "q-bio.NC" (Quantitative Biology - Neurons and Cognition)
3. Загрузить файлы
4. Заполнить метаданные
5. Отправить на модерацию

### 3. МЕТАДАННЫЕ

#### Title:
"First Optical Connectome Analysis of Human Brain: A Novel Framework for Bio-photonic Communication Networks"

#### Authors:
[Ваше имя], Optical Connectome Research Team

#### Abstract:
[Использовать из arxiv_preprint_final_updated.md]

#### Keywords:
optical connectome, bio-photonic communication, brain connectivity, diffusion MRI, waveguide modeling

#### Categories:
q-bio.NC, physics.bio-ph, cs.NE

### 4. ОЖИДАНИЕ МОДЕРАЦИИ

#### Время:
- Обычно: 1-3 дня
- Пиковое время: до 1 недели

#### Статус:
- Отправлено → В модерации → Принято/Отклонено

### 5. ПОСЛЕ ПРИНЯТИЯ

#### Получить:
- arXiv ID (например: 2412.00001)
- URL: https://arxiv.org/abs/2412.00001
- PDF: https://arxiv.org/pdf/2412.00001.pdf

#### Обновить:
- GitHub README с ссылкой на arXiv
- Zenodo с ссылкой на arXiv
- Все документы с arXiv ID

## 🚀 ГОТОВО!

После загрузки:
- ✅ Приоритет защищен
- ✅ Работа доступна публично
- ✅ Можно ссылаться в других работах
- ✅ Готово к подаче в журналы

## ⏱️ ВРЕМЯ ВЫПОЛНЕНИЯ

- Подготовка файлов: 10 мин
- Загрузка на arXiv: 15 мин
- **ИТОГО: ~25 мин**

## 🎯 ГОТОВЫ НАЧИНАТЬ?

1. **Обновить рукопись** с DOI и GitHub
2. **Создать архив** для arXiv
3. **Загрузить** на arXiv
4. **Ждать модерации**

**Начинаем?** 🚀
"""
    
    with open('ARXIV_UPLOAD_INSTRUCTIONS.md', 'w') as f:
        f.write(instructions)
    
    print("✅ Инструкции для arXiv созданы: ARXIV_UPLOAD_INSTRUCTIONS.md")

def main():
    """Основная функция"""
    print("📝 ШАБЛОН ДЛЯ ОБНОВЛЕНИЯ РУКОПИСИ")
    print("=" * 40)
    
    # Пример использования
    print("Для обновления рукописи выполните:")
    print("python3 update_manuscript_template.py")
    print()
    print("Или вручную замените в arxiv_preprint_final.md:")
    print("1. DOI: [ЗАМЕНИТЬ НА РЕАЛЬНЫЙ DOI]")
    print("2. GitHub URL: [ЗАМЕНИТЬ НА РЕАЛЬНЫЙ URL]")
    print()
    
    # Создаем инструкции для arXiv
    create_arxiv_upload_instructions()
    
    print("✅ Шаблон готов!")
    print("📁 Созданные файлы:")
    print("   - ARXIV_UPLOAD_INSTRUCTIONS.md")
    print("   - update_manuscript_template.py")

if __name__ == "__main__":
    main()
