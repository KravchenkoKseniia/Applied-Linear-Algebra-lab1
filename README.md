# Applied-Linear-Algebra-lab1

## Theoretical questions

[1. Що таке лінійні трансформації? ](#pa1) 

[2. Як і в яких галузях застосовуються лінійні трансформації?](#pa2)  

[3. Що таке матриця лінійної трансформації та як її можна інтерпретувати?](#pa3)  

[4. Які особливості та властивості має матриця обертання?](#pa4)

[5. Чи залежить фінальний результат від порядку трансформацій? Провести експерименти з фігурами або зображеннями з частин 1-2.](#pa5)

[6. Була здійснена якась довільна лінійна трансформація; як знайти матрицю лінійної трансформації, що поверне все до початкового вигляду? Чи завжди можна здійснити обернену трансформацію? ](#pa6) 

[7. Модуль визначника матриці трансформації менше 1, які висновки можна зробити про дану трансформацію (як змінюється простір при даній трансформації)? А якщо більше 1? Дорівнює 1? Дорівнює 0? ](#pa7)


<a name = "pa1"></a>
### Що таке лінійні трансформації?
Перш за все, варто зрозуміти, що трансформації, це, по суті, те саме, що й функції. Тобто, це те, що приймає на вхід число. Але, якщо ми функції описуємо графіками, то коли ми говоримо саме про трансформації, то маємо на увазі візуальні дії над об'єктом: розтягування, стискання, відзеркалювання тощо. Крім того, говорячи в контексті лінійних трансформацій, ми приймаємо н вході один вектор, на виході отримуємо інший вектор. Трансформації, що називаються лінійні мають обмеження, а саме: всі лінії мають залишатись лініями після трансформації та початок координат має залишатись незмінним як до, так і після трансформації.


<a name = "pa2"></a>
### Як і в яких галузях застосовуються лінійні трансформації?
Лінійні трансформації застосовуються у багатьох сферах діяльності: фізика, робототехніка, комп'ютерна графіка, економіка, комп'ютерні науки, обробка даних тощо. Ось кілька прикладів їх застосування у реальному житті:
- Анімація і 3Д-графіка. Лінійні трансформації є ключовим інструментом для керування і перетворення об'єктів у віртуальному просторі: масштабування, обертання, переміщення тощо.
- Економіка. В економічному моделюванні для зв'язків між різними змінними, що допомагає розуміти та прогнозувати різні економічні тенденції та рішення.
- Системи керування та робототехніка. Лінійні трансформації використовуються для моделювання руху та поведінки роботів чи інших систем, також допомагають керувати та проектувати складними механічними системами.

Приклади взяти з даного джерела: https://www.quora.com/What-are-some-real-life-applications-of-linear-transformations-and-how-can-we-identify-them#:~:text=They%20are%20used%20in%20a,and%20enhance%20images%20and%20signals%20.


<a name = "pa3"></a>
### Що таке матриця лінійної трансформації та як її можна інтерпретувати?
Матриця лінійної трансформації - це матриця, совпчиками якої є координати лінійного перетворення образів одного базису одного простору в іншому базису в іншому просторі. Таке представлення є зручним з боку обчислень. Матриці лінійної трансформації, проте, визначаються неоднозначно, адже залежать від обраних базисів з використанням матриць переходу. Дану матрицю можна інтерпретувати як опис дій цієї матриці на базисні вектори. Крім того, ми можемо розглядати її як операції перетворення об'єкту (наприклад нашого об'єкту, який ми створюємо яерез np.array):
- Поворот
- Відображення
- Відзеркалення
- Масштабування


<a name = "pa4"></a>
### Які особливості та властивості має матриця обертання?
Особливість даної матриці полягає в тому, що дана матриця є ортогональною матрицею - невироджена матриця А, така що A * А^T = I, де І - одинична матриця. Також еквівалентним буде твердження: А^T = A^-1, тобто обернена матриця до А дорівнює її транспонованій матриці. Крім того, оскільки A * А^T  множить рядки А проти себе,  і А^T * А - стовпці проти себе, то рядки та стовпці А мають утворювати нормований та ортогональний набір векторів. Тобто, помноживши дані вектори один проти одного, ми отримаємо 1. А помноживши різні рядки, ми отримаємо 0. Ба більше, існує ще одна особливість таких матриць: 
Якщо ми розглянемо матрицю А, помножену на довільних вектор-стовпчик х, то ми отримаємо (Ах)^T * Ax =
