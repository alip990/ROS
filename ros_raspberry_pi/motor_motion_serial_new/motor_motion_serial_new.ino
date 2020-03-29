const int pwm_1 = 5;
const int m_11 = 6;
const int m_12 = 7;


const int m_21 = 8;
const int m_22 = 9;
const int pwm_2 = 10;

void setup()
{
  pinMode(pwm_1, OUTPUT);
  pinMode(m_11, OUTPUT);
  pinMode(m_12, OUTPUT);
  
  pinMode(pwm_2 , OUTPUT);
  pinMode(m_21, OUTPUT);
  pinMode(m_22, OUTPUT);
  Serial.begin(9600);
}

void global_init(int a_11, int a_12, int a_21, int a_22)
{
  analogWrite(pwm_1, 150);
  digitalWrite(m_11, a_11);
  digitalWrite(m_12, a_12);
  
  analogWrite(pwm_2, 150);
  digitalWrite(m_21, a_21);
  digitalWrite(m_22, a_22);
}

void forword(void)
{
  global_init(1,0, 1,0);
}

void backword(void)
{
  global_init(0,1, 0,1);
}
void all_stop(void)
{
  global_init(0,0, 0,0);
}
void f_r(void)
{
  global_init(0,0, 1,0);
}
void f_l(void)
{
  global_init(1,0, 0,0);
}

void b_r(void)
{
  global_init(0,0, 0,1);
}

void b_l(void)
{
  global_init(0,1, 0,0);
}


void loop()
{
  if(Serial.read()=='F')
  {
    forword();
    delay(100);
  }
  if(Serial.read()=='B')
  {
    backword();
    delay(100);
  }
  else
  {
    all_stop();
  }
  
}
