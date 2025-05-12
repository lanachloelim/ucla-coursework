// Actually, a line must contain MAX_LINE_LEN-2 chars at most
#define MAX_LINE_LEN 100000
// Actually, a clause must contain MAX_CLAUSE_LEN-1 literals at most
#define MAX_CLAUSE_LEN 1025
// maximum size of a label string: used for printing clauses, var sets, etc/
#define STRING_LABEL_SIZE 1024

#define KB 1024
#define MB 1048576
#define GB 1073741824
//#define rprintf printf //for MS VCC
#define rprintf(format, args...) ( printf("c "), printf(format , ## args), fflush(stdout) )

#define FIRST_RESTART 100
#define INITIAL_RESTART_INCR 100 //how many backtracks to increment by
#define RESTART_INCR_INCR 0 //add to the restart_incr by this amount each time
#define RESTART_MULTIPLIER 1.5

#define MAX_LEARNED_CLAUSES_MULTIPLIER 1.5
#define CLAUSE_SCORE_INC_FACTOR 1.001001001001001001001001001001 //based on minisat (1/0.999)
#define LEARNED_CLAUSE_FACTOR 0.7
#define NEXT_SIMPLIFY_INCREMENT 0

//END added globals

//Knot added 12/6/05

#define SCORE_INC_FACTOR 1.052632  //based on minisat
#define SCORE_INC_PARAM 0.95 

#define SCORE_LIMIT 1e100
#define CLAUSE_SCORE_LIMIT 1e20
#define SCORE_DIVIDER 1e-100  //must == 1/score_limit
#define CLAUSE_SCORE_DIVIDER 1e-20 //must == 1/clause_score_limit

#define INIT_RANDOM_SEED 91648253 //from minisat
#define RANDOM_VAR_FREQ 0.02 //from minisat
//end Knot added

#define CONSERVATIVE_KB_REDUCTION_FACTOR 0.5
#define SAVE_PROGRESS_RECENTNESS_THRESHOLD 0.4  //the higher this number, the more we save
#define VC_THRESHOLD 100000
#define LUBY_UNIT 512

#define INIT_ON_TH 100
#define INIT_ON_TH_INC 0
#define INIT_OFF_TH 400
#define INIT_OFF_TH_INC 0
