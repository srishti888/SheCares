function Card() {
    return (
      <div className="flex justify-center items-center min-h-screen bg-gray-100 z-1">
        <div className="card w-full max-w-md bg-gradient-to-br from-[rgba(210,217,222,0.5)] to-[rgba(210,217,222,0.2)] shadow-lg backdrop-blur-sm rounded-2xl p-8 z-10">
          
          <form className="space-y-6">
            <div>
              <h1 className="card_title text-center text-2xl font-bold text-[#433335]">
                login to sheCares
              </h1>
            </div>

            <div className="space-y-2">
              <p className="text-sm font-semibold text-[#433335]">Your Email</p>
              <input
                type="email"
                placeholder="Enter email"
                className="w-full h-10 px-4 bg-gradient-to-r from-[rgba(215,224,232,0.8)] to-[rgba(215,224,232,0.8)] rounded-md outline-none focus:ring-2 focus:ring-[#433335]"
              />
            </div>

            <div className="space-y-2">
              <p className="text-sm font-semibold text-[#433335]">Your Password</p>
              <input
                type="password"
                placeholder="Enter password"
                className="w-full h-10 px-4 bg-gradient-to-r from-[rgba(215,224,232,0.8)] to-[rgba(215,224,232,0.8)] rounded-md outline-none focus:ring-2 focus:ring-[#433335]"
              />
            </div>

            <div className="flex justify-between items-center">
              <a href="#" className="text-sm font-medium text-[#433335]">
                Forgot?
              </a>
            </div>

            <button
              type="submit"
              className="w-full h-10 bg-gradient-to-r from-[rgba(139,87,92,0.56)] to-[rgba(139,87,92,0.8)] rounded-md text-white font-bold text-sm"
            >
              Login
            </button>

            <div className="text-center space-y-2">
              <p className="text-sm text-[#433335]">Don't have an account?</p>
              <button
                type="button"
                className="w-full h-10 bg-gradient-to-r from-[rgba(139,87,92,0.56)] to-[rgba(139,87,92,0.8)] rounded-md text-white font-bold text-sm"
              >
                Sign Up
              </button>
              
            </div>
          </form>
        </div>
      </div>
    );
  }
  
  export default Card;
  
