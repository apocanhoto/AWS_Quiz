from question import question

question_prompts = [
	"What is AWS?\n(a)Amazon Web Services\n(b)2\n(c)3 \n",
	"What is IAM?\n(a)Identity Authentication Manager\n(b)Identity and Access Management\n(c)Identity and Authentication Manager\n",
	"What is EC2?\n(a)1\n(b)2\n(c)3 \n",
	"What is EC2?\n(a)1\n(b)2\n(c)3 \n",
	"What is EC2?\n(a)1\n(b)2\n(c)3 \n",
	"What is EC2?\n(a)1\n(b)2\n(c)3 \n",
	"What is EC2?\n(a)1\n(b)2\n(c)3 \n",
]

questions = [
	question(question_prompts[0], "a"),
	question(question_prompts[1], "b"),
	question(question_prompts[2], "c"),
]


def run_test(questions):
	score = 0
	for question in questions:
		answer = input(question.prompt)
		if answer == question.answer:
			score += 1
			print("Yes!\n")
		else:
			print("please review.\n")
	print("You got "+ str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)











